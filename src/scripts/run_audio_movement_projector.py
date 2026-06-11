#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


import os

from src.model_managers.model_file_manager import ModelFileManager
from src.streamers.audio_movement_streamer import AudioMovementStreamer
from src.trainers.train_audio_movement_projector import train_audio_movement_projector
from src.utils import make_name_unique

from run_settings import RunSettings


def run_audio_movement_projector(run_settings=RunSettings()):
    model_file_manager = ModelFileManager()
    if model_file_manager.does_pretrained_model_exist(
        pretrained_model_path=run_settings.audio_movement_projector_settings.PRETRAINED_MODEL_PATH,
        submodule_path='shared_latent_space_projector.pt',
    ):
        model_path = run_settings.audio_movement_projector_settings.PRETRAINED_MODEL_PATH
    else:
        model_path = make_name_unique('output_data_runs/')
        os.mkdir(model_path)
        os.mkdir(f"{model_path}/model")
        if run_settings.logging_settings.ENABLE_MODEL_METADATA_LOGGING:
            os.mkdir(f"{model_path}/model_metadata")
            with open(f"{model_path}/model_metadata/run_settings.txt", 'w') as f:
                f.write(f"RUN_SETTINGS: '{run_settings}'\n")
        audio_movement_projector = train_audio_movement_projector(
            output_dir_path=model_path,
            run_settings=run_settings,
        )
        model_file_manager.save_model(audio_movement_projector=audio_movement_projector, output_dir_name=f"{model_path}/model/")
        
    AudioMovementStreamer(run_settings=run_settings).stream_movement_to_audio(
        model_dir=model_path,
        python_play_audio=run_settings.audio_movement_projector_settings.PYTHON_PLAY_AUDIO,
        audio_frames_per_chunk=run_settings.audio_movement_projector_settings.AUDIO_FRAMES_PER_CHUNK,
        tambereen_interface_path=run_settings.MAX_INTERFACE_PATH,
    )


if __name__ == '__main__':
    run_audio_movement_projector()
