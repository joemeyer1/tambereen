
from dataclasses import dataclass

import numpy as np


@dataclass
class MovementChunk:
    frames: np.ndarray
