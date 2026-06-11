
from dataclasses import dataclass
from typing import Optional

from src.time_chunks.AudioChunk import AudioChunk
from src.time_chunks.KeypointsChunk import KeypointsChunk
from src.time_chunks.MovementChunk import MovementChunk


@dataclass
class TimeChunk:
    movement_chunk: Optional[MovementChunk] = None
    keypoints_chunk: Optional[KeypointsChunk] = None
    audio_chunk: Optional[AudioChunk] = None
