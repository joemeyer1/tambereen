#!/usr/bin/env python3
# Copyright (c) 2024 Joseph Meyer. All Rights Reserved.

from collections import OrderedDict
from typing import Optional

import torch
from torch import nn

from src.projectors.data_normalizer import DataNormalizer

torch.set_grad_enabled(False)


class AutoEncoder(nn.Module):

    data_normalizer: Optional[DataNormalizer] = None

    def __init__(self, input_dim: int, dense_dim: int, output_dim: int):

        super(AutoEncoder, self).__init__()

        encoder = nn.Sequential(
            nn.Linear(input_dim, dense_dim),
            nn.ReLU(),
            nn.Linear(dense_dim, output_dim),
        )

        decoder = nn.Sequential(
            nn.Linear(output_dim, dense_dim),
            nn.ReLU(),
            nn.Linear(dense_dim, input_dim),
        )

        self.net = nn.Sequential(OrderedDict([
            ('encoder', encoder),
            ('decoder', decoder),
        ]))

    def embed(self, x: torch.Tensor) -> torch.Tensor:
        normalized_x = self.normalize_data(x)
        return self.net.encoder(normalized_x)

    def decode(self, embedding: torch.Tensor) -> torch.Tensor:
        net_output = self.net.decoder(embedding)
        denormalized_net_output = self.denormalize_data(net_output)
        return denormalized_net_output

    def forward(self, x: torch.Tensor):
        normalized_embedding = self.embed(x)
        return self.decode(normalized_embedding)

    def normalize_data(self, data: torch.Tensor) -> torch.Tensor:
        if self.data_normalizer is not None:
            return self.data_normalizer.normalize_data(data)
        else:
            return data

    def denormalize_data(self, data: torch.Tensor) -> torch.Tensor:
        if self.data_normalizer is not None:
            return self.data_normalizer.denormalize_data(data)
        else:
            return data
