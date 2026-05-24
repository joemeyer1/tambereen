#!/usr/bin/env python3
# Copyright (c) 2024 Joseph Meyer. All Rights Reserved.


from tests.test_autoencode_audio import test_autoencode_audio
from tests.test_keypoints_extractor import test_keypoints_extractor
from tests.test_keypoints_encoder import test_keypoints_encoder
from tests.test_train_audio_movement_projector import test_train_audio_movement_projector
from tests.test_audio_novelifier import test_audio_novelifier
from tests.test_finetuning import test_finetuning

from run_settings import RunSettings, AudioMovementProjectorSettings, AudioNovelifierSettings


def run_all_tests():
    test_autoencode_audio(audio_file_path='../../audio_training_data/percussion/banana-shaker__long_forte_shaken.wav')
    test_keypoints_extractor(keypoints_dataset_filename="keypoints_data_test.csv", max_frames=100)
    test_keypoints_encoder(epochs=4, max_frames=25)
    test_train_audio_movement_projector(run_settings=RunSettings(audio_movement_projector_settings=AudioMovementProjectorSettings(EPOCHS=4, MAX_AUDIO_SECS=3)))
    test_audio_novelifier(run_settings=RunSettings(audio_novelifier_settings=AudioNovelifierSettings(EPOCHS=4, MAX_AUDIO_SECS=3)))
    test_finetuning(run_settings=RunSettings(audio_movement_projector_settings=AudioMovementProjectorSettings(EPOCHS=4, MAX_AUDIO_SECS=3)))


if __name__ == '__main__':
    run_all_tests()
