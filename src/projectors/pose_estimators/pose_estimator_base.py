#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


import numpy as np


class PoseEstimatorBase:
    min_confidence_threshold: float
    kp_dim: float  # keypoints dimensions (i.e. number of keypoints)

    def get_keypoints(self, frame) -> np.ndarray:
        raise NotImplementedError
