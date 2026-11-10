#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


from typing import Any, Optional

import numpy as np
import soundfile as sf
import torch
from torch import nn

from run_settings import RunSettings

torch.set_grad_enabled(False)


class AudioProjector(nn.Module):
    audio_projector: Optional[Any]  # Can be either RAVE or SAO model (as they use same API), loaded as a pytorch '.ts' 

    def __init__(self, audio_projector: Optional[Any] = None):
        nn.Module.__init__(self)

        self.audio_projector = audio_projector

    def embed_audio(self, audio_data: np.ndarray) -> torch.Tensor:
        """Embed audio into latent audio space."""

        print(f"Embedding audio data...")

        if self.audio_projector is None:
            raise RuntimeError("An audio projector must be configured before embedding audio.")

        audio_projector_device = next(self.audio_projector.parameters()).device
        if RunSettings._is_stable_audio:
            if RunSettings._is_stable_audio_3:
                audio_data = audio_data[:len(audio_data) - len(audio_data)%8192]
            audio_data = torch.from_numpy(audio_data).reshape(1, 1, -1)
            audio_data = torch.tile(audio_data, (1, 2, 1)).to(audio_projector_device)
        else:  # RAVE - mono
            audio_data = torch.from_numpy(audio_data).reshape(1, 1, -1).to(audio_projector_device)
        # audio_data = torch.from_numpy(audio_data[:len(audio_data) - len(audio_data)%8192]).reshape(1, 1, -1)
        # audio_data = torch.tile(audio_data, (1, 2, 1)).to(audio_projector_device)
        # print(f"audio_data.shape: {audio_data.shape}")
        return torch.t(self.audio_projector.encode(audio_data)[0])

    def autoencode_audio(self, audio_data: np.ndarray, sample_rate: int, audio_output_file_path: str) -> None:

        if self.audio_projector is None:
            raise RuntimeError("An audio projector must be configured before autoencoding audio.")

        audio_projector_device = next(self.audio_projector.parameters()).device
        audio_data = torch.from_numpy(audio_data).reshape(1, 1, -1).to(audio_projector_device)
        audio_embeddings = self.audio_projector.encode(audio_data)
        autoencoded_audio = self.decode_audio_embs(audio_embeddings).detach().cpu().numpy().reshape(-1)

        sf.write(audio_output_file_path, autoencoded_audio, sample_rate)
