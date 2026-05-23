#!/usr/bin/env python3
# Copyright (c) 2024 Joseph Meyer. All Rights Reserved.


import pandas as pd

from src.streamers.movement_streamer import MovementStreamer


def test_keypoints_extractor(
        keypoints_dataset_filename: str,
        max_frames: int,
) -> None:
    """Record yourself dancing in front of computer to create dataset."""

    keypoints_data_for_training = MovementStreamer().record_keypoints(max_frames=max_frames)
    pd.DataFrame(keypoints_data_for_training).to_csv(keypoints_dataset_filename)


if __name__ == '__main__':
    test_keypoints_extractor(keypoints_dataset_filename="keypoints_data_test.csv", max_frames=100)
