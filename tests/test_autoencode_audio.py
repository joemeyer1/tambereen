#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.

import numpy as np

import librosa as li

from src.model_managers.rave_loader import RaveLoader
from src.trainers.train_audio_movement_projector import AudioMovementProjector

from src.utils import play_audio


def test_autoencode_audio(audio_file_path: str = 'audio_training_data/percussion/banana-shaker__long_forte_shaken.wav') -> None:

    # play_audio(audio_file_path)  # play original audio for comparison

    rave_model = RaveLoader().download_official_model_by_name('percussion')
    movement_to_sound_generator = AudioMovementProjector(audio_projector=rave_model)

    audio_data, sample_rate = li.load(audio_file_path, sr=44100)
    # sample_rate, audio_data = wavfile.read(audio_file_path)

    if audio_data.ndim > 1:
        audio_data = np.mean(audio_data, 1)

    autoencoded_audio_file_path = f"autoencoded_{audio_file_path.split('/')[-1]}"
    movement_to_sound_generator.autoencode_audio(audio_data=audio_data, sample_rate=sample_rate, audio_output_file_path=autoencoded_audio_file_path)
    play_audio(autoencoded_audio_file_path)  # play autoencoded audio


if __name__ == '__main__':
    test_autoencode_audio(audio_file_path='audio_training_data/percussion/banana-shaker__long_forte_shaken.wav')

