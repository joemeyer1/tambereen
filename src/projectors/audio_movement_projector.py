#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


from typing import Any, Optional

import numpy as np
import torch
from torch import nn

from src.time_chunks.KeypointsChunk import KeypointsChunk
from src.time_chunks.AudioChunk import AudioChunk

from src.projectors.movement_projector import MovementProjector
from src.projectors.keypoints_projector import KeypointsProjector
from src.projectors.audio_projector import AudioProjector

from pythonosc.udp_client import SimpleUDPClient

OSC_IP = "127.0.0.1"
OSC_PORT = 7004

torch.set_grad_enabled(False)


class AudioMovementProjector(MovementProjector, KeypointsProjector, AudioProjector, nn.Module):
    audio_projector: Optional[Any]  # todo - I think this is actually a pytorch recursive script model?
    movement_projector: Optional[Any]  # todo - I think this is maybe a tf Interpreter?
    keypoints_projector: Optional[nn.Module]
    multimodal_projector: Optional[nn.Module]

    def __init__(
            self,
            audio_projector: Optional[Any] = None,
            movement_projector: Optional[Any] = None,
            keypoints_projector: Optional[nn.Module] = None,
            multimodal_projector: Optional[nn.Module] = None,
            novelifier: Optional[nn.Module] = None,
    ):

        nn.Module.__init__(self)

        self.audio_projector = audio_projector
        self.movement_projector = movement_projector
        self.keypoints_projector = keypoints_projector
        self.multimodal_projector = multimodal_projector
        self.novelifier = novelifier

        self.osc = SimpleUDPClient(OSC_IP, OSC_PORT)
        self.address = "/emb"

    def proj_audio_into_multimodal_space(self, audio_data: np.ndarray, max_audio_frames: Optional[int] = None) -> torch.Tensor:
        """Projects audio data into shared audio-movement latent space."""

        audio_embeddings = self.embed_audio(audio_data)
        if max_audio_frames is not None:
            audio_embeddings = audio_embeddings[:max_audio_frames]
        latent_audio = torch.stack([self.multimodal_projector.embed(audio_embedding) for audio_embedding in audio_embeddings])
        return latent_audio

    def proj_keypoints_into_multimodal_space(self, keypoints_data: torch.Tensor) -> torch.Tensor:
        """Projects keypoints into shared audio-movement space."""

        keypoints_embeddings = self.encode_keypoints(keypoints_data=keypoints_data)
        multimodal_movement_embeddings = torch.stack([self.multimodal_projector.embed(keypoints_embedding) for keypoints_embedding in keypoints_embeddings])
        return multimodal_movement_embeddings

    def proj_keypoints_to_audio_embs(self, keypoints_chunk: KeypointsChunk, osc_stream_audio: bool = True) -> AudioChunk:
        """Projects keypoints into shared audio-movement space, then decodes to audio embeddings.

        Usually raw and novelified audio embeddings will be streamed to Max MSP patch, which will decode them (while providing an interface to mix raw and novelified signals). If Max MSP is not available, set osc_stream_audio to False to avoid unnecessary port streaming via osc; in that case streamers.audio_player can be used to play audio directly via Python instead. Note that novelified audio mixing is only available when streaming to the Max interface, not when playing audio directly in python (which has no mechanism for interactive interpolation).
        
        Args:
            keypoints_chunk: Contains keypoints for a chunk of time frames.
            osc_stream_audio: If True, sends audio embeddings via osc for Max MSP streaming.
        
        Returns:
            Audio embeddings mapped to from keypoints.
        
        """

        multimodal_movement_embeddings = self.proj_keypoints_into_multimodal_space(keypoints_data=keypoints_chunk.frames)
        audio_embeddings = self.multimodal_projector.decode(multimodal_movement_embeddings)

        if osc_stream_audio:
            if self.novelifier is not None:
                audio_embeddings_novelified = torch.squeeze(self.novelifier.forward(audio_embeddings))
                audio_embedding_novelified_str = ' '.join(str(i) for i in audio_embeddings_novelified.tolist())
                self.osc.send_message(f"{self.address}_novel", audio_embedding_novelified_str)

            audio_embeddings = torch.squeeze(audio_embeddings, dim=1)
            audio_embedding_str = ' '.join(str(i) for i in audio_embeddings.tolist())
            self.osc.send_message(self.address, audio_embedding_str)
            if self.novelifier is None:
                self.osc.send_message(f"{self.address}_novel", audio_embedding_str)
            print(audio_embedding_str)
        else:
            audio_embeddings = torch.squeeze(audio_embeddings, dim=1)

        return AudioChunk(embedding_frames=audio_embeddings)
    
    def decode_audio_embs(self, audio_embs: torch.Tensor) -> torch.Tensor:
        decoded_audio = self.audio_projector.decode(audio_embs)
        decoded_audio = torch.mean(decoded_audio, dim=1, keepdim=True)  # convert to mono
        return decoded_audio
