#!/usr/bin/env python3
# Copyright (c) 2024 Joseph Meyer. All Rights Reserved.


import os

from src.model_managers.model_file_manager import ModelFileManager
from src.streamers.audio_movement_streamer import AudioMovementStreamer
from src.trainers.supervised_finetune_audio_movement_projector import supervised_finetune_audio_movement_projector
from src.utils import make_name_unique

from run_settings import RunSettings, AudioMovementProjectorSettings


def test_finetuning(model_dirname: str = 'output_data_runs/0', finetuning_path: str = 'ground_ctrl.mp4', run_settings: RunSettings = RunSettings(audio_novelifier_settings=AudioMovementProjectorSettings(EPOCHS=10))) -> None:
    output_dir_path = make_name_unique('output_data_runs/')
    os.mkdir(output_dir_path)

    if run_settings.audio_movement_projector_settings.MAX_AUDIO_SECS is not None:
        RAVE_EMBS_PER_SEC = 2048
        max_training_frames = int(run_settings.audio_movement_projector_settings.MAX_AUDIO_SECS * RAVE_EMBS_PER_SEC)
    else:
        max_training_frames = None

    finetuned_model = supervised_finetune_audio_movement_projector(model_dirname=model_dirname, training_data_filename=finetuning_path, epochs=run_settings.audio_movement_projector_settings.EPOCHS, max_movement_frames=max_training_frames)
    ModelFileManager.save_model(audio_movement_projector=finetuned_model, output_dir_name=f"{output_dir_path}/model/")

    if run_settings.logging_settings.ENABLE_MODEL_METADATA_LOGGING:
        os.mkdir(f"{output_dir_path}/model_metadata")
        with open(f"{output_dir_path}/model_metadata/run_settings.txt", 'w') as f:
            f.write(f"RUN_SETTINGS: '{run_settings}'\n\nModel finetuned on data: '{finetuning_path}' from pretrained model '{model_dirname}'\n")

    print("Testing finetuned_model...")
    AudioMovementStreamer(run_settings=run_settings).stream_movement_to_audio(
        model_dir=output_dir_path,
        python_play_audio=run_settings.audio_movement_projector_settings.PYTHON_PLAY_AUDIO,
        audio_frames_per_chunk=run_settings.audio_movement_projector_settings.AUDIO_FRAMES_PER_CHUNK,
        tambereen_interface_path=run_settings.MAX_INTERFACE_PATH,
    )


if __name__ == '__main__':
    test_finetuning()

