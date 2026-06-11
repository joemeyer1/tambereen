#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.

import os
from typing import Tuple, Optional, Union

import numpy as np
import sounddevice as sd
import soundfile as sf
import torch
from torch.utils.data import Dataset


def make_name_unique(name: str) -> str:

    def get_last_dot_i(name) -> Optional[int]:
        j_range = list(range(1, len(name)))
        j_range.reverse()
        for j in j_range:
            if name[j] == '.':
                return j
        return None

    last_dot_i = get_last_dot_i(name)
    if last_dot_i:
        raw_name, ext = name[:last_dot_i], name[last_dot_i:]
    else:
        raw_name, ext = name, ''
    i = 0
    while os.path.exists(raw_name + str(i) + ext):
        i += 1
    return raw_name + str(i) + ext


def resize_tensor(tensor_to_resize: torch.Tensor, new_length: int) -> torch.Tensor:

    print(f"resizing tensor from length {tensor_to_resize.shape[0]} to {new_length}")

    # downsample if new length is shorter than current length
    if tensor_to_resize.shape[0] >= new_length:
        return tensor_to_resize[:new_length]

    # upsample otherwise
    n_tiles = int(np.ceil(new_length / len(tensor_to_resize)))
    return torch.tile(tensor_to_resize, (n_tiles, 1))[:new_length]


def get_audio_data(audio_dir_paths: Union[str, Tuple[str, ...]] = 'audio_training_data/percussion', max_audio_frames: Optional[float] = None) -> Tuple[np.ndarray, int]:
    print(f"max_audio_frames: {max_audio_frames}")
    audio_data = []
    audio_sample_rate = 0
    if type(audio_dir_paths) is str:
        audio_dir_paths = (audio_dir_paths,)
    for audio_dir_path in audio_dir_paths:
        for audio_filename in os.listdir(audio_dir_path):
            max_audio_frames_reached = max_audio_frames is not None and sum(len(audio_file_data) for audio_file_data in audio_data) >= max_audio_frames
            if max_audio_frames_reached:
                return np.concatenate(audio_data)[:max_audio_frames], audio_sample_rate
            else:
                audio_filepath = f"{audio_dir_path}/{audio_filename}"
                try:
                    audio_file_data, audio_sample_rate = sf.read(audio_filepath, dtype='float32')
                    if audio_file_data.ndim > 1:
                        assert audio_file_data.ndim == 2
                        audio_file_data = np.mean(audio_file_data, axis=1)
                    audio_data.append(audio_file_data)
                except Exception as e:
                    print(e)
                    print(f"Couldn't read audio data from file '{audio_dir_path}/{audio_filename}'")
    assert len(audio_data) > 0
    audio_data = np.concatenate(audio_data)
    if max_audio_frames is not None:
        audio_data = audio_data[:max_audio_frames]
    return audio_data, audio_sample_rate


def play_audio(file_path: str, wait_for_playback_to_finish: bool = False):
    audio_data, audio_sample_rate = sf.read(file_path)
    sd.play(audio_data, audio_sample_rate)
    if wait_for_playback_to_finish:
        sd.wait()


def convert_mp3_to_wav(existing_mp3_folder: str, new_wav_folder: str) -> None:
    from pydub import AudioSegment

    for audio_filename in os.listdir(existing_mp3_folder):
        from_audio_filepath = f"{existing_mp3_folder}/{audio_filename}"
        audio_filepath = f"{new_wav_folder}/{audio_filename.replace('mp3','wav')}"
        sound = AudioSegment.from_mp3(from_audio_filepath)
        sound.export(audio_filepath, format="wav")


class CustomDataset(Dataset):
    def __init__(self, data: torch.Tensor, metadata: Optional[torch.Tensor] = None):
        self.data = data
        self.metadata = metadata

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if self.metadata is not None:
            return self.data[idx], self.metadata[idx]
        else:
            return self.data[idx]

    def split(self, split_ratio: float) -> Tuple[Dataset, Dataset]:
        split_i = int(split_ratio * len(self.data))
        print(f"splitting data ({len(self.data) - split_i}, {split_i})")
        if self.metadata is not None:
            return CustomDataset(data=self.data[split_i:], metadata=self.metadata[split_i:]), CustomDataset(data=self.data[:split_i], metadata=self.metadata[:split_i])
        else:
            return CustomDataset(data=self.data[split_i:]), CustomDataset(data=self.data[:split_i])

    def shuffle(self):
        self.data = self.data[torch.randperm(self.data.shape[0])]
        if self.metadata is not None:
            self.metadata = self.metadata[torch.randperm(self.metadata.shape[0])]
