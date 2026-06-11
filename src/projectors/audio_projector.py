#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


from typing import Any, Optional

import numpy as np
import soundfile as sf
import torch
from torch import nn

torch.set_grad_enabled(False)


class AudioProjector(nn.Module):
    audio_projector: Optional[Any]  # todo - I think this is actually a pytorch recursive script model?

    def __init__(self, audio_projector: Optional[Any] = None):
        nn.Module.__init__(self)

        self.audio_projector = audio_projector

    def embed_audio(self, audio_data: np.ndarray) -> torch.Tensor:
        """Embed audio into latent audio space."""

        print(f"Embedding audio data...")

        audio_data = torch.from_numpy(audio_data).reshape(1, 1, -1)
        return torch.t(self.audio_projector.encode(audio_data)[0])

    def autoencode_audio(self, audio_data: np.ndarray, sample_rate: int, audio_output_file_path: str) -> None:

        audio_data = torch.from_numpy(audio_data).reshape(1, 1, -1)
        audio_embeddings = self.audio_projector.encode(audio_data)
        autoencoded_audio = self.decode_audio_embs(audio_embeddings).numpy().reshape(-1)

        sf.write(audio_output_file_path, autoencoded_audio, sample_rate)
