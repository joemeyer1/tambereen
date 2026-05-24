#!/usr/bin/env python3
# Copyright (c) 2024 Joseph Meyer. All Rights Reserved.

from typing import Optional

import ffmpeg


def test_redub(
    video_path: str = "output_data_runs/0/soundless_movement_output/interact_movement0.mp4",
    audio_path: str = "output_data_runs/0/audio_output/interact_movement_to_audio0_novelified0.mp4",
    output_path: Optional[str] = None,
):

    if output_path is None:
        output_path = f"{video_path.split('.')[0].split('/')[-1]}_{audio_path.split('.')[0].split('/')[-1]}.mp4"

    audio_stream = ffmpeg.input(audio_path).audio
    video_stream = ffmpeg.input(video_path).video
    ffmpeg.output(video_stream, audio_stream, output_path).run(capture_stderr=True)


if __name__ == '__main__':
    test_redub()
