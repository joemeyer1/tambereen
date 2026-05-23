#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. All Rights Reserved.


from typing import List

import cv2
import mediapipe as mp

import numpy as np

from src.projectors.pose_estimators.pose_estimator_base import PoseEstimatorBase


class PoseEstimatorMediapipe(PoseEstimatorBase):
    def __init__(self, pose: bool = True, hands: bool = True, num_hands: int = 2, min_confidence_threshold: float = 0.5):

        self.num_hands = num_hands
        self.min_confidence_threshold = min_confidence_threshold

        self.hands = mp.solutions.hands.Hands(
            min_detection_confidence=min_confidence_threshold,
            min_tracking_confidence=min_confidence_threshold,
            max_num_hands=num_hands,
        ) if hands else None

        self.pose = mp.solutions.pose.Pose(  # mediapipe uses BlazePose for body pose estimation
            min_detection_confidence=min_confidence_threshold,
            min_tracking_confidence=min_confidence_threshold,
        ) if pose else None

        self.hands_results = None
        self.pose_results = None

        self.kp_dim = 0
        if hands:
            self.kp_dim += 21 * num_hands
        if pose:
            self.kp_dim += 33

    def estimate_pose(self, frame) -> None:
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if self.hands is not None:
            self.hands_results = self.hands.process(imgRGB)
        if self.pose is not None:
            self.pose_results = self.pose.process(imgRGB)

    def extract_keypoints(self, frame, draw=True) -> List[float]:
        keypoints_yx = []
        if self.pose is not None:
            keypoints_yx += self.extract_pose_keypoints(frame, draw)
        if self.hands is not None:
            keypoints_yx += self.extract_hands_keypoints(frame, draw)
        return keypoints_yx

    def extract_pose_keypoints(self, frame, draw=True):
        xList =[]
        yList =[]
        keypoints_yx = [0] * 33 * 2
        if self.pose_results is not None:
            if self.pose_results.pose_landmarks:
                h, w, c = frame.shape
                if draw:
                    mp.solutions.drawing_utils.draw_landmarks(frame, self.pose_results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
                for lm_id, lm in enumerate(self.pose_results.pose_landmarks.landmark):
                    if lm.visibility >= self.min_confidence_threshold:
                        
                        cx, cy = int(lm.x * w), int(lm.y * h)

                        xList.append(cx)
                        yList.append(cy)
                        kp_ix_start = lm_id * 2
                        keypoints_yx[kp_ix_start: kp_ix_start + 2] = [lm.y, lm.x]
                        if draw:
                            cv2.circle(
                                img=frame,
                                center=(cx, cy),
                                radius=5,
                                color=(255, 0, 255),
                                thickness=cv2.FILLED,
                            )
                            
                    # if draw:
                    #     cv2.rectangle(
                    #         img=frame,
                    #         pt1=(min(xList) - 20, min(yList) - 20),
                    #         pt2=(max(xList) + 20, max(yList) + 20),
                    #         color=(0, 255, 0),
                    #         thickness=2,
                    #     )

        return keypoints_yx

    def extract_hands_keypoints(self, frame, draw=True):
        xList =[]
        yList =[]
        keypoints_yx = [0] * (21 * self.num_hands * 2)

        if self.hands_results is not None:
            if self.hands_results.multi_hand_landmarks:
                h, w, c = frame.shape
                for hand_landmarks, handedness in zip(self.hands_results.multi_hand_landmarks, self.hands_results.multi_handedness):
                    hand_id = int(handedness.classification[0].label == 'Right')  # 0: left, 1: right
                    if draw:
                        mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
                    for lm_id, lm in enumerate(hand_landmarks.landmark):
                        cx, cy = int(lm.x * w), int(lm.y * h)

                        xList.append(cx)
                        yList.append(cy)
                        kp_ix_start = (lm_id * 2) + (hand_id * 21 * 2)
                        keypoints_yx[kp_ix_start: kp_ix_start + 2] = [lm.y, lm.x]
                        if draw:
                            cv2.circle(
                                img=frame,
                                center=(cx, cy),
                                radius=5,
                                color=(255, 0, 255),
                                thickness=cv2.FILLED,
                            )
                            
                    # if draw:
                    #     cv2.rectangle(
                    #         img=frame,
                    #         pt1=(min(xList) - 20, min(yList) - 20),
                    #         pt2=(max(xList) + 20, max(yList) + 20),
                    #         color=(0, 255, 0),
                    #         thickness=2,
                    #     )

        return keypoints_yx

    def get_keypoints(self, frame) -> np.ndarray:
        self.estimate_pose(frame)
        keypoints = self.extract_keypoints(frame)
        return np.array(keypoints).reshape(1, len(keypoints))
