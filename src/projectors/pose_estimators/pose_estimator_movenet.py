#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. All Rights Reserved.


import numpy as np
import tensorflow as tf

from src.projectors.pose_estimators.pose_estimator_base import PoseEstimatorBase
from src.streamers.draw_keypoints import draw_keypoints, draw_connections


class PoseEstimatorMoveNet(PoseEstimatorBase):
    def __init__(self, model_path: str = 'pretrained_model_checkpoints/movenet_checkpoints/3.tflite', min_confidence_threshold: float = 0.1):

        self.min_confidence_threshold = min_confidence_threshold
        self.kp_dim = 17

        self.movenet = tf.lite.Interpreter(model_path=model_path)
        self.movenet.allocate_tensors()

    def get_keypoints(self, frame) -> np.ndarray:

        input_image = self._format_frame(frame.copy())

        # Setup input and output
        input_details = self.movenet.get_input_details()
        output_details = self.movenet.get_output_details()

        # Make predictions
        self.movenet.set_tensor(input_details[0]['index'], input_image)
        self.movenet.invoke()
        keypoints_with_scores = self.movenet.get_tensor(output_details[0]['index'])

        # zero out low-confidence keypoints
        keypoints_with_scores[np.where(keypoints_with_scores[:, :, :, 2] < self.min_confidence_threshold)] = 0

        keypoints_yx = keypoints_with_scores[:, :, :, :2].reshape(1, keypoints_with_scores.shape[2] * 2)  # take first 2 columns (y, x), hence *2

        # Rendering
        draw_connections(frame, keypoints=keypoints_with_scores)
        draw_keypoints(frame, keypoints=keypoints_with_scores)

        return keypoints_yx

    @staticmethod
    def _format_frame(frame):
        # Reshape image
        resized_frame = tf.image.resize_with_pad(np.expand_dims(frame, axis=0), 192, 192)
        formatted_frame = tf.cast(resized_frame, dtype=tf.float32)
        return formatted_frame

