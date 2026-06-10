#!/usr/bin/env python3
# Copyright (c) 2026 Joseph Meyer. MIT License.


from dataclasses import dataclass
from typing import Optional

from src.projectors.pose_estimators.pose_estimator_base import PoseEstimatorBase
from src.projectors.pose_estimators.pose_estimator_movenet import PoseEstimatorMoveNet
from src.projectors.pose_estimators.pose_estimator_mediapipe import PoseEstimatorMediapipe


RAVE_MODEL: str  = 'percussion'  # This should be the same for audio-movement projector and audio novelifier
# see src.model_managers.rave_loader
# use RaveLoader.load_model_from_file_path(model_file_path=RAVE_MODEL) if you want to load from RAVE_MODEL file path instead of using an official IRCAM model
# (but if the  RAVE_MODEL is not an official IRCAM model then the standard function will load it from local path anyway)

_RAVE_MODEL_INTERFACES = {
    'percussion': 'interfaces/tambereen_interface_percussion.maxpat',
    'musicnet': 'interfaces/tambereen_interface_musicnet.maxpat',
    'VCTK': 'interfaces/tambereen_interface_vctk.maxpat',
}

MAX_INTERFACE_PATH: str = _RAVE_MODEL_INTERFACES[RAVE_MODEL]


@dataclass
class LoggingSettings:
    # LoggingParams indicates what data to save (model itself will always be saved after training because otherwise it can't be used, but saving anything else is optional)
    # Data is only logged to the local device running the program
    ENABLE_AUDIO_LOGGING: bool = True  # Warning: If ENABLE_AUDIO_LOGGING=False, audio you generate will NOT be saved
    ENABLE_MOVEMENT_LOGGING: bool = True  # If ENABLE_MOVEMENT_LOGGING=True, video of your movements will be recorded
    ENABLE_MODEL_METADATA_LOGGING: bool = True  # If ENABLE_MODEL_METADATA_LOGGING=True, logs model description (e.g. paths of training data, training settings, etc.) and objective over training epochs (this flag is relevant for training only)
    ENABLE_DEBUG_LOGGING: bool = False  # If ENABLE_DEBUG_LOGGING=True, intermediate representations like training embeddings and keypoints will be logged (which is useful for troubleshooting)


@dataclass
class PoseEstimatorSettings:
    POSE_ESTIMATOR_TYPE: PoseEstimatorBase = PoseEstimatorMoveNet  # class PoseEstimatorMoveNet (faster) or PoseEstimatorMediapipe (can model hands, more universal compatibility)

    # Below two settings only apply for PoseEstimatorMediapipe
    MEDIAPIPE_USE_POSE: bool = True
    MEDIAPIPE_USE_HANDS: bool = True

    MOVENET_PATH: str = 'pretrained_model_checkpoints/movenet_checkpoints/3.tflite'  # only applies for PoseEstimatorMoveNet

@dataclass
class AudioMovementProjectorSettings:
    PRETRAINED_MODEL_PATH: Optional[str] = None  # If you use a pre-trained model, make sure POSE_ESTIMATOR_TYPE aligns
    # If you try using a different pose estimator than the model was trained with, the pose keypoints passed won't align with those the model was trained with and you will get a tensor size mismatch error between actual input and model input dimensions

    PYTHON_PLAY_AUDIO: bool = False
    AUDIO_FRAMES_PER_CHUNK: int = 1

    pose_estimator_settings: PoseEstimatorSettings = PoseEstimatorSettings()

    AUDIO_TRAINING_DATA_PATH: str = 'audio_training_data/percussion'
    USE_CACHE: bool = False  # For training data
    MAX_AUDIO_SECS: Optional[float] = 30

    EPOCHS: int = 200
    LEARNING_RATE: float = 0.001
    TEST_DATA_FRACTION: float = 0.2  # fraction of data to set aside for test metrics (must be nonzero for overfit detection)



@dataclass
class AudioNovelifierSettings:
    PRETRAINED_MODEL_PATH: Optional[str] = None
    
    AUDIO_TRAINING_DATA_PATH: str = 'audio_training_data/percussion'
    USE_CACHE: bool = False  # For training data
    MAX_AUDIO_SECS: Optional[float] = 30

    EPOCHS: int = 200
    LEARNING_RATE: float = 0.001
    TEST_DATA_FRACTION: float = 0.2

    MUTE_DURING_TRAINING: bool = True


@dataclass
class RunSettings:
    audio_movement_projector_settings: Optional[AudioMovementProjectorSettings] = AudioMovementProjectorSettings()
    audio_novelifier_settings: Optional[AudioNovelifierSettings] = AudioNovelifierSettings()
    logging_settings: Optional[LoggingSettings] = LoggingSettings()
    RAVE_MODEL: Optional[str] = RAVE_MODEL
    MAX_INTERFACE_PATH: Optional[str] = MAX_INTERFACE_PATH

