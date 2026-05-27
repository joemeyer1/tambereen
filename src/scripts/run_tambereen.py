#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


import os

import torch

from src.model_managers.model_file_manager import ModelFileManager
from src.streamers.audio_movement_streamer import AudioMovementStreamer
from src.trainers.train_audio_movement_projector import train_audio_movement_projector
from src.trainers.train_audio_novelifier import train_audio_novelifier
from src.utils import make_name_unique

from run_settings import RunSettings


def run_tambereen(run_settings=RunSettings()):
    model_file_manager = ModelFileManager()
    if model_file_manager.are_all_models_pretrained_in_unified_folder(run_settings=run_settings):
        model_path = run_settings.audio_movement_projector_settings.PRETRAINED_MODEL_PATH
    else:
        model_path  = make_name_unique('output_data_runs/')
        os.mkdir(model_path)
        os.mkdir(f"{model_path}/model")
        if run_settings.logging_settings.ENABLE_MODEL_METADATA_LOGGING:
            os.mkdir(f"{model_path}/model_metadata")
            with open(f"{model_path}/model_metadata/run_settings.txt", 'w') as f:
                f.write(f"RUN_SETTINGS: '{run_settings}'\n")
        if model_file_manager.does_pretrained_model_exist(
            pretrained_model_path=run_settings.audio_movement_projector_settings.PRETRAINED_MODEL_PATH,
            submodule_path='shared_latent_space_projector.pt',
        ):
            for submodule in ('audio_projector.pt', 'keypoints_projector.pt', 'shared_latent_space_projector.pt'):
                print(f"loading audio-movement projector {run_settings.audio_movement_projector_settings.PRETRAINED_MODEL_PATH}/model/{submodule}")
                os.system(f"cp {run_settings.audio_movement_projector_settings.PRETRAINED_MODEL_PATH}/model/{submodule} {model_path}/model/{submodule}")
        else:
            audio_movement_projector = train_audio_movement_projector(
                output_dir_path=model_path,
                run_settings=run_settings,
            )
            model_file_manager.save_model(audio_movement_projector=audio_movement_projector, output_dir_name=f"{model_path}/model/")
        
        if model_file_manager.does_pretrained_model_exist(
            pretrained_model_path=run_settings.audio_novelifier_settings.PRETRAINED_MODEL_PATH,
            submodule_path='audio_novelifier.pt',
        ):
            print(f"loading {run_settings.audio_novelifier_settings.PRETRAINED_MODEL_PATH}/model/audio_novelifier.pt")
            os.system(f"cp {run_settings.audio_novelifier_settings.PRETRAINED_MODEL_PATH}/model/audio_novelifier.pt {model_path}/model/audio_novelifier.pt")
        else:
            print("Training audio_novelifier...")
            audio_novelifier = train_audio_novelifier(
                run_settings=run_settings,
                batch_size=10,
                shuffle_each_epoch=True,
                output_dir_path=model_path,
            )
            torch.save(audio_novelifier, f'{model_path}/model/audio_novelifier.pt')

    AudioMovementStreamer(run_settings=run_settings).stream_movement_to_audio(
        model_dir=model_path,
        python_play_audio=run_settings.audio_movement_projector_settings.PYTHON_PLAY_AUDIO,
        audio_frames_per_chunk=run_settings.audio_movement_projector_settings.AUDIO_FRAMES_PER_CHUNK,
        tambereen_interface_path=run_settings.MAX_INTERFACE_PATH,
    )


if __name__ == '__main__':
    run_tambereen()
