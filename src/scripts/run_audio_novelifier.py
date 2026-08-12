#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


import os
from typing import Optional

import sounddevice as sd
import soundfile as sf

import numpy as np
import pandas as pd
import torch

from src.model_managers.rave_loader import RaveLoader
from src.trainers.train_audio_novelifier import train_audio_novelifier
from src.utils import get_audio_data, make_name_unique

from run_settings import RunSettings, AudioNovelifierSettings


def run_audio_novelifier(
        run_settings: RunSettings = RunSettings(
            RAVE_MODEL='percussion',
            audio_novelifier_settings=AudioNovelifierSettings(PRETRAINED_MODEL_PATH=None, AUDIO_TRAINING_DATA_PATH='audio_training_data/percussion', EPOCHS=10),
        ),
        test_audio_data_path: str = 'audio_training_data/percussion',
):

    pretrained_rave_model = RaveLoader().download_official_model_by_name(model_name=run_settings.RAVE_MODEL)

    # GET AUDIO_NOVELIFIER
    pretrained_novelifier_path = run_settings.audio_novelifier_settings.AudioNovelifierSettings.PRETRAINED_MODEL_PATH
    if pretrained_novelifier_path is not None and os.path.exists(pretrained_novelifier_path):
        pretrained_audio_novelifier_path = f"{pretrained_novelifier_path}/model/audio_novelifier.pt"
        assert os.path.exists(pretrained_audio_novelifier_path)
        print(f"loading {pretrained_audio_novelifier_path}")
        audio_novelifier = torch.load(f"{pretrained_audio_novelifier_path}")

        output_dir_path = pretrained_novelifier_path
    else:
        output_dir_path = make_name_unique('output_data_runs/')
        os.mkdir(output_dir_path)
        os.mkdir(f"{output_dir_path}/model/")
        os.mkdir(f"{output_dir_path}/samples/")

        print("Training audio_novelifier...")
        audio_novelifier = train_audio_novelifier(
            run_settings=run_settings,
            batch_size=10,
            shuffle_each_epoch=True,
            output_dir_path=output_dir_path,
        )
        torch.save(audio_novelifier, f'{output_dir_path}/model/audio_novelifier.pt')

    print(f"Testing audio_novelifier ({output_dir_path.replace('output_data_runs/', '')})...")
    if not os.path.exists(f"{output_dir_path}/samples/"):
        os.mkdir(f"{output_dir_path}/samples/")
    novelified_samples_dir_path = make_name_unique(f"{output_dir_path}/samples/")
        
    # GET AUDIO DATA FOR TEST
    if run_settings.audio_novelifier_settings.MAX_AUDIO_SECS is not None and run_settings.audio_novelifier_settings.MAX_AUDIO_SECS > 0:
        samples_per_sec = 44100
        max_audio_frames = int(run_settings.audio_novelifier_settings.MAX_AUDIO_SECS * samples_per_sec)
    else:
        max_audio_frames = None
    audio_data, audio_sample_rate = get_audio_data(audio_dir_paths=test_audio_data_path, max_audio_frames=max_audio_frames)

    if len(audio_data.shape) > 1:  # convert to mono
        audio_data = audio_data.mean(1)

    # Encode test data
    audio_data = torch.from_numpy(audio_data).reshape(1, 1, -1)
    audio_embeddings = pretrained_rave_model.encode(audio_data)
    print(f"audio_embeddings.shape: {audio_embeddings.shape}")
    if run_settings.logging_settings.ENABLE_DEBUG_LOGGING:
        pd.DataFrame(audio_embeddings[0]).to_csv("audio_embeddings.csv")


    # Decode test data
    audio_output_file_path = f'{novelified_samples_dir_path}/autoencoded_audio.wav'
    if not os.path.exists(audio_output_file_path):
        autoencoded_audio = pretrained_rave_model.decode(audio_embeddings).numpy().reshape(-1)
        sf.write(audio_output_file_path, autoencoded_audio, audio_sample_rate)

    # Novelify then decode embeddings
    pre_novelified_audio_embeddings = audio_embeddings.transpose(1, 2)
    novelified_audio_embeddings = audio_novelifier.forward(pre_novelified_audio_embeddings).transpose(1, 2)
    pd.DataFrame(novelified_audio_embeddings[0]).to_csv("novelified_audio_embeddings.csv")

    # write incrementally novelified audio
    incrementally_novelified_audio_list = []
    for novelification_ratio in (float(i / 20) for i in range(0, 21)):
        mixed_audio_embeddings = (novelification_ratio * novelified_audio_embeddings) + ((1 - novelification_ratio) * audio_embeddings)
        mixed_audio = pretrained_rave_model.decode(mixed_audio_embeddings).numpy().reshape(-1)

        novelification_ratio_str = str(np.round(novelification_ratio, 3)).replace('.', ',')
        novelified_filename = make_name_unique(f"{novelified_samples_dir_path}/{novelification_ratio_str}_novelified_audio.wav")
        sf.write(novelified_filename, mixed_audio, audio_sample_rate)
        incrementally_novelified_audio_list.append(mixed_audio)
    incrementally_novelified_audio = np.concatenate(incrementally_novelified_audio_list, axis=0)
    sf.write(make_name_unique(f"incrementally_novelified_audio.wav"), incrementally_novelified_audio, audio_sample_rate)
    print(f"Done.\n\n")


if __name__ == '__main__':
    run_audio_novelifier()
