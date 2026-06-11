
from dataclasses import dataclass

import torch

torch.set_grad_enabled(False)


@dataclass
class KeypointsChunk:
    frames: torch.Tensor
