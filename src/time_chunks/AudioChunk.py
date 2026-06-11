
from dataclasses import dataclass
from typing import Optional

from torch import Tensor


@dataclass
class AudioChunk:
    embedding_frames: Optional[Tensor]
    wav_data: Optional[Tensor] = None
