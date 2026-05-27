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


def test_audio_novelifier(
        novel_wet_ratio_embeddings: float = 1,
        novel_wet_ratio_audio: float = 1,
        run_settings: RunSettings = RunSettings(audio_novelifier_settings=AudioNovelifierSettings(EPOCHS=10)),
        pretrained_model_path: Optional[str] = None,
):

    assert 0 <= novel_wet_ratio_embeddings <= 1
    assert 0 <= novel_wet_ratio_audio <= 1

    # rave_model_name, audio_dir_paths = 'musicnet', 'audio_training_data/bach'
    rave_model_name, audio_dir_paths = 'percussion', 'audio_training_data/percussion'

    pretrained_rave_model = RaveLoader().download_official_model_by_name(model_name=rave_model_name)

    # GET AUDIO_NOVELIFIER
    if pretrained_model_path is not None and os.path.exists(pretrained_model_path):
        pretrained_audio_novelifier_path = f"{pretrained_model_path}/model/audio_novelifier.pt"
        assert os.path.exists(pretrained_audio_novelifier_path)
        print(f"loading {pretrained_audio_novelifier_path}")
        audio_novelifier = torch.load(f"{pretrained_audio_novelifier_path}")
        if not os.path.exists(f"{pretrained_model_path}/samples/"):
            os.mkdir(f"{pretrained_model_path}/samples/")
        output_dir_path = pretrained_model_path
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

    # GET AUDIO DATA FOR TEST
    if run_settings.audio_novelifier_settings.MAX_AUDIO_SECS is not None and run_settings.audio_novelifier_settings.MAX_AUDIO_SECS > 0:
        samples_per_sec = 44100
        max_audio_frames = int(run_settings.audio_novelifier_settings.MAX_AUDIO_SECS * samples_per_sec)
    else:
        max_audio_frames = None
    audio_data, audio_sample_rate = get_audio_data(audio_dir_paths=audio_dir_paths, max_audio_frames=max_audio_frames)

    if len(audio_data.shape) > 1:  # convert to mono
        audio_data = audio_data.mean(1)

    # ENCODE AUDIO DATA
    audio_data = torch.from_numpy(audio_data).reshape(1, 1, -1)
    audio_embeddings = pretrained_rave_model.encode(audio_data)
    print(f"audio_embeddings.shape: {audio_embeddings.shape}")
    pd.DataFrame(audio_embeddings[0]).to_csv("audio_embeddings.csv")


    # GENERATE TEST DATA
    audio_output_file_path = f'{output_dir_path}/samples/autoencoded_audio.wav'
    if not os.path.exists(audio_output_file_path):
        autoencoded_audio = pretrained_rave_model.decode(audio_embeddings).numpy().reshape(-1)
        sf.write(audio_output_file_path, autoencoded_audio, audio_sample_rate)

    # Novelify then decode embeddings
    pre_novelified_audio_embeddings = audio_embeddings.transpose(1, 2)
    novelified_audio_embeddings = audio_novelifier.forward(pre_novelified_audio_embeddings).transpose(1, 2)
    pd.DataFrame(novelified_audio_embeddings[0]).to_csv("novelified_audio_embeddings.csv")

    if novel_wet_ratio_embeddings < 1:  # add some dry signal to embedding
        balanced_audio_embeddings = (novel_wet_ratio_embeddings * novelified_audio_embeddings) + ((1 - novel_wet_ratio_embeddings) * audio_embeddings)
        balanced_audio = pretrained_rave_model.decode(balanced_audio_embeddings)

        balanced_audio_embeddings_prime = pretrained_rave_model.encode(balanced_audio)
        pd.DataFrame(balanced_audio_embeddings_prime[0]).to_csv("balanced_audio_embeddings_prime.csv")

        balanced_audio = balanced_audio.numpy().reshape(-1)

        novelified_audio_embeddings = balanced_audio_embeddings


    if novel_wet_ratio_audio < 1:  # add some dry signal to audio output

        novelified_audio = pretrained_rave_model.decode(novelified_audio_embeddings)

        novelified_audio_embeddings_prime = pretrained_rave_model.encode(novelified_audio)
        pd.DataFrame(novelified_audio_embeddings_prime[0]).to_csv("novelified_audio_embeddings_prime.csv")

        np_audio_novel = novelified_audio.numpy().reshape(-1)
        np_audio_raw = audio_data.numpy().reshape(-1)
        min_audio_length = min(len(np_audio_novel), len(np_audio_raw))
        balanced_audio = novel_wet_ratio_audio * np_audio_novel[:min_audio_length] + \
                           (1 - novel_wet_ratio_audio) * np_audio_raw[:min_audio_length]

    if novel_wet_ratio_audio == 1 and novel_wet_ratio_embeddings == 1:  # all wet novelified
        balanced_audio = pretrained_rave_model.decode(novelified_audio_embeddings).numpy().reshape(-1)

    novel_wet_ratio_embeddings_str = str(np.round(novel_wet_ratio_embeddings, 3)).replace('.', ',')
    novel_wet_ratio_audio_str = str(np.round(novel_wet_ratio_audio, 3)).replace('.', ',')
    novelified_filename = make_name_unique(f"{output_dir_path}/samples/{novel_wet_ratio_embeddings_str}_{novel_wet_ratio_audio_str}_novelified_audio.wav")
    sf.write(novelified_filename, balanced_audio, audio_sample_rate)


    # PLAY OUTPUT
    print(f"Novelified: ", end='', flush=True)
    try:
        sd.play(balanced_audio, audio_sample_rate)
        sd.wait()
    except KeyboardInterrupt as e:
        print(e)
    print(f"Done.\n\n")
    print(output_dir_path.replace('output_data_runs/', ''), '\n\n')

    print(f"Auteoncoded Original: ", end='', flush=True)
    try:
        sd.play(autoencoded_audio, audio_sample_rate)
        sd.wait()
    except KeyboardInterrupt as e:
        print(e)
    print(f"Done.\n\n")

    print(f"Raw Original: ", end='', flush=True)
    try:
        sd.play(audio_data.reshape(-1).numpy(), audio_sample_rate)
        sd.wait()
    except KeyboardInterrupt as e:
        print(e)
    print(f"Done.\n\n")


if __name__ == '__main__':
    test_audio_novelifier()
