#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


import os

from src.model_managers.model_file_manager import ModelFileManager
from src.streamers.audio_movement_streamer import AudioMovementStreamer
from src.trainers.train_audio_movement_projector import train_audio_movement_projector
from src.utils import make_name_unique

from run_settings import RunSettings, AudioMovementProjectorSettings


def test_train_audio_movement_projector(
        interact: bool = True,
        run_settings=RunSettings(audio_movement_projector_settings=AudioMovementProjectorSettings(EPOCHS=10)),
    ):
    output_dir_path = make_name_unique('output_data_runs/')
    os.mkdir(output_dir_path)
    audio_movement_projector = train_audio_movement_projector(
        output_dir_path=output_dir_path,
        run_settings=run_settings,
    )

    ModelFileManager.save_model(audio_movement_projector=audio_movement_projector, output_dir_name=f"{output_dir_path}/model/")
    
    if interact:
        print("Testing movement_to_sound_generator...")
        AudioMovementStreamer().stream_movement_to_audio(
        model_dir=output_dir_path,
        python_play_audio=AudioMovementProjectorSettings.PYTHON_PLAY_AUDIO,
        chunk_buffer_size=AudioMovementProjectorSettings.CHUNK_BUFFER_SIZE,
        tambereen_interface_path=RunSettings.MAX_INTERFACE_PATH,
    )
