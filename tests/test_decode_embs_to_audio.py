#!/usr/bin/env python3
# Copyright (c) 2024 Joseph Meyer. All Rights Reserved.


from time import sleep

import soundfile as sf
import torch

from src.model_managers.rave_loader import RaveLoader
from src.utils import play_audio

torch.set_grad_enabled(False)


def test_decode_embs_to_audio() -> None:
    """Tests RAVE audio generation from random latent vectors."""

    rave_model_percussion = RaveLoader().download_official_model_by_name('percussion')
    percussion_dim = 4

    rave_model_musicnet = RaveLoader().download_official_model_by_name('musicnet')
    musicnet_dim = 16

    for rave_model, rave_dim in (
            (rave_model_percussion, percussion_dim),
            (rave_model_musicnet, musicnet_dim),
    ):

        for x in (
            torch.zeros(size=(1, 1, rave_dim)),
            torch.ones(size=(1, 1, rave_dim)),
            torch.randn(size=(1, 1, rave_dim)),
            torch.randint(low=-10, high=10, size=(1, 1, rave_dim)).float(),
        ):
            y = rave_model.decode(x)
            sf.write('trash.wav', y.numpy().reshape(-1), 44100)
            play_audio('trash.wav', wait_for_playback_to_finish=True)
            sleep(1)


if __name__ == '__main__':
    test_decode_embs_to_audio()
