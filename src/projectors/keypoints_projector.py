#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


from typing import Optional

import torch
from torch import nn

torch.set_grad_enabled(False)


class KeypointsProjector(nn.Module):
    """Projects keypoints into a latent space."""

    keypoints_projector: Optional[nn.Module]

    def __init__(self, keypoints_projector: Optional[nn.Module] = None,):
        nn.Module.__init__(self)

        self.keypoints_projector = keypoints_projector

    def encode_keypoints(self, keypoints_data: torch.Tensor) -> torch.Tensor:
        encoded_keypoints_data = torch.stack([self.keypoints_projector.embed(keypoints_frame) for keypoints_frame in keypoints_data])
        return encoded_keypoints_data
