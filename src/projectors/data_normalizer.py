# Copyright (c) 2025 Joseph Meyer. All Rights Reserved.
#!/usr/bin/env python3


from typing import Optional

import torch


torch.set_grad_enabled(False)


class DataNormalizer:
    def __init__(self, data: torch.tensor, eps: float = 1e-12, col_scale_factors: Optional[torch.tensor] = None):

        self.col_avgs = torch.mean(data, dim=0)
        self.col_stds = torch.std(data, dim=0)

        self.col_scale_factors = self.col_stds if col_scale_factors is None else col_scale_factors
        self.col_scale_factors += eps  # avoid div-by-0

    def normalize_data(self, data: torch.Tensor) -> torch.Tensor:
        return (data - self.col_avgs) / self.col_scale_factors

    def denormalize_data(self, data: torch.Tensor) -> torch.Tensor:
        return (data * self.col_scale_factors) + self.col_avgs
