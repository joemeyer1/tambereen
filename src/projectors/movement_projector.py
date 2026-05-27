#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


import numpy as np
import torch
from torch import nn

from src.time_chunks.MovementChunk import MovementChunk
from src.time_chunks.KeypointsChunk import KeypointsChunk

from src.projectors.pose_estimators.pose_estimator_base import PoseEstimatorBase
from src.projectors.pose_estimators.pose_estimator_mediapipe import PoseEstimatorMediapipe
from src.projectors.pose_estimators.pose_estimator_movenet import PoseEstimatorMoveNet

from run_settings import AudioMovementProjectorSettings

torch.set_grad_enabled(False)


class MovementProjector(nn.Module):
    """Projects movement into keypoints."""

    pose_estimator: PoseEstimatorBase

    def __init__(self):
        nn.Module.__init__(self)

    def load_movement_projector(self, audio_movement_projector_settings: AudioMovementProjectorSettings = AudioMovementProjectorSettings()):

        pose_estimator_type: PoseEstimatorBase = audio_movement_projector_settings.pose_estimator_settings.POSE_ESTIMATOR_TYPE

        if pose_estimator_type == PoseEstimatorMediapipe:                
            self.pose_estimator = PoseEstimatorMediapipe(pose=audio_movement_projector_settings.pose_estimator_settings.MEDIAPIPE_USE_POSE, hands=audio_movement_projector_settings.pose_estimator_settings.MEDIAPIPE_USE_HANDS)
        else:
            assert pose_estimator_type == PoseEstimatorMoveNet, f"POSE_ESTIMATOR_TYPE must be 'PoseEstimatorMediapipe' or 'PoseEstimatorMoveNet', not '{pose_estimator_type}'"
            self.pose_estimator = PoseEstimatorMoveNet(model_path='pretrained_model_checkpoints/movenet_checkpoints/3.tflite')

    def proj_movement_chunk_to_keypoints(self, movement_chunk: MovementChunk) -> KeypointsChunk:
        keypoints_frames = [self.proj_movement_frame_to_keypoints(movement_frame=frame) for frame in movement_chunk.frames]
        return KeypointsChunk(torch.tensor(np.concatenate(keypoints_frames)))

    def proj_movement_frame_to_keypoints(self, movement_frame: np.ndarray) -> np.ndarray:
        return self.pose_estimator.get_keypoints(movement_frame)
