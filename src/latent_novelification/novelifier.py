#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. All Rights Reserved.


from typing import List, Optional

import torch
from torch import nn

from src.projectors.data_normalizer import DataNormalizer

torch.set_grad_enabled(False)


class Novelifier(nn.Module):

    submodules: Optional[nn.ModuleDict]
    supermodule: nn.Module
    data_normalizer: Optional[DataNormalizer] = None

    def __init__(self, latent_dim: int, dense_dim: int, submodule_names: Optional[List[str]] = None):

        super(Novelifier, self).__init__()

        self.latent_dim = latent_dim

        if submodule_names is not None and len(submodule_names) > 0:
            self.submodules = nn.ModuleDict({name: nn.Sequential(
                nn.Linear(latent_dim, dense_dim),
                nn.ReLU(),
                nn.Linear(dense_dim, latent_dim),
            ) for name in submodule_names})

            self.supermodule = nn.Sequential(
                nn.Linear(latent_dim * (len(submodule_names) + 1), dense_dim),
                nn.ReLU(),
                nn.Linear(dense_dim, latent_dim),
            )
        else:
            self.submodules = None
            self.supermodule = nn.Sequential(
                nn.Linear(latent_dim, dense_dim),
                nn.ReLU(),
                nn.Linear(dense_dim, latent_dim),
            )

    def forward(self, embedding: torch.Tensor, submodule_name: Optional[str] = None) -> torch.Tensor:
        if self.submodules is None:
            return self.supermodule(embedding)
        else:
            if submodule_name is not None and submodule_name in self.submodules:
                submodule = self.submodules[submodule_name]
                submodule_i = list(self.submodules.keys()).index(submodule_name)
                submodules_output = torch.nn.functional.pad(submodule(embedding), pad=(self.latent_dim * submodule_i, self.latent_dim * (len(self.submodules) - submodule_i - 1)))
            else:
                submodules_output = torch.cat([submodule(embedding) for submodule in self.submodules.values()], -1)

            supermodule_input = torch.cat([embedding, submodules_output], dim=-1)
            return self.supermodule(supermodule_input)

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
