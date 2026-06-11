#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


from run_settings import RunSettings, AudioMovementProjectorSettings, AudioNovelifierSettings

from src.scripts.run_tambereen import run_tambereen


def test_tambereen():
    run_settings=RunSettings(
        audio_movement_projector_settings=AudioMovementProjectorSettings(PRETRAINED_MODEL_PATH=None, EPOCHS=10, MAX_AUDIO_SECS=3),
        audio_novelifier_settings=AudioNovelifierSettings(PRETRAINED_MODEL_PATH=None, EPOCHS=10, MAX_AUDIO_SECS=3),
    )
    return run_tambereen(run_settings=run_settings)

if __name__ == '__main__':
    test_tambereen()
