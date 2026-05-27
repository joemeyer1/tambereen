#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


from src.streamers.audio_movement_streamer import AudioMovementStreamer
from run_settings import RunSettings, AudioMovementProjectorSettings


def test_interact_from_pretrained(model_dir_path: str):
    AudioMovementStreamer().stream_movement_to_audio(
        model_dir=model_dir_path,
        python_play_audio=AudioMovementProjectorSettings.PYTHON_PLAY_AUDIO,
        audio_frames_per_chunk=AudioMovementProjectorSettings.AUDIO_FRAMES_PER_CHUNK,
        tambereen_interface_path=RunSettings.MAX_INTERFACE_PATH,
    )



if __name__ == '__main__':
    test_interact_from_pretrained(model_dir_path='output_data_runs/0')
