#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


import os
from typing import Optional

import pandas as pd
import torch

from src.model_managers.rave_loader import RaveLoader
from src.projectors.audio_movement_projector import AudioMovementProjector
from src.projectors.data_normalizer import DataNormalizer
from src.streamers.movement_streamer import MovementStreamer
from src.trainers.train_autoencoder import train_autoencoder
from src.utils import get_audio_data, resize_tensor
from run_settings import RunSettings


def train_audio_movement_projector(output_dir_path: str, run_settings: RunSettings) -> AudioMovementProjector:

    if not os.path.exists(output_dir_path):
        os.mkdir(output_dir_path)

    # rave_model_name, audio_dir_paths = 'percussion', 'audio_training_data/percussion'
    # rave_model_name, audio_dir_paths = 'musicnet', 'audio_training_data/violin'
    rave_model_name, audio_dir_paths = run_settings.RAVE_MODEL, run_settings.audio_movement_projector_settings.AUDIO_TRAINING_DATA_PATH

    pretrained_rave_model = RaveLoader().download_official_model_by_name(model_name=rave_model_name)

    RAVE_EMBS_PER_SEC = 2048
    if run_settings.audio_movement_projector_settings.MAX_AUDIO_SECS is not None:
        max_training_frames = int(run_settings.audio_movement_projector_settings.MAX_AUDIO_SECS * RAVE_EMBS_PER_SEC)
    else:
        max_training_frames = None
    
    audio_embeddings_cache_path = f"{'/'.join(audio_dir_paths.split('/')[:-1])}/_cached_embeddings/" \
                                  f"{audio_dir_paths.split('/')[-1]}.pt"
    if run_settings.audio_movement_projector_settings.USE_CACHE and os.path.exists(audio_embeddings_cache_path):
        print(f"Loading cached audio embeddings...")
        audio_embeddings = torch.load(audio_embeddings_cache_path)
        if max_training_frames is not None:
            audio_embeddings = audio_embeddings[:max_training_frames]
    else:
        audio_data, audio_sample_rate = get_audio_data(audio_dir_paths=audio_dir_paths, max_audio_frames=max_training_frames)

        # encode audio
        audio_embeddings = AudioMovementProjector(audio_projector=pretrained_rave_model).embed_audio(audio_data)
        print(f"Caching audio embeddings...")
        if not os.path.exists(f"{'/'.join(audio_embeddings_cache_path.split('/')[:-1])}"):
            os.mkdir(f"{'/'.join(audio_embeddings_cache_path.split('/')[:-1])}")
        torch.save(audio_embeddings, audio_embeddings_cache_path)

    print("Training keypoints encoder...")
    # extract keypoints (e.g. with MoveNet) to train keypoints encoder on
    # sd.play(audio_data, audio_sample_rate)
    keypoints_data_for_training = MovementStreamer(run_settings=run_settings).record_keypoints(
        max_frames=max_training_frames,
        output_filename=f"{output_dir_path}/movement_training_data.mp4",
    )
    # sd.stop()
    if run_settings.logging_settings.ENABLE_DEBUG_LOGGING:
        pd.DataFrame(keypoints_data_for_training).to_csv("keypoints_data_for_training.csv")

    keypoints_normalizer = DataNormalizer(keypoints_data_for_training)  # , null_value=torch.nan)
    normalized_keypoints_data_for_training = keypoints_normalizer.normalize_data(keypoints_data_for_training)

    if run_settings.logging_settings.ENABLE_DEBUG_LOGGING:
        pd.DataFrame(normalized_keypoints_data_for_training).to_csv('normalized_keypoints_data_for_training.csv')

    # train encoder to project keypoints into a latent space of same dimension as RAVE's latent space (e.g. "4")
    keypoints_projector = train_autoencoder(
        input_dim=normalized_keypoints_data_for_training.shape[1],
        dense_dim=24,
        output_dim=audio_embeddings.shape[1],
        training_data=normalized_keypoints_data_for_training,
        epochs=run_settings.audio_movement_projector_settings.EPOCHS,
        batch_size=1,
        shuffle_each_epoch=True,
        enable_model_metadata_logging=run_settings.logging_settings.ENABLE_MODEL_METADATA_LOGGING,
        test_fraction=run_settings.audio_movement_projector_settings.TEST_DATA_FRACTION,
        model_name='keypoints encoder',
        output_dir_path=output_dir_path,
    )
    keypoints_projector.data_normalizer = keypoints_normalizer

    print("Training shared audio-movement space projector...")

    # encode keypoints
    keypoints_embeddings_for_training = AudioMovementProjector(keypoints_projector=keypoints_projector).encode_keypoints(keypoints_data=keypoints_data_for_training)

    if run_settings.logging_settings.ENABLE_DEBUG_LOGGING:
        pd.DataFrame(audio_embeddings).to_csv('audio_embeddings.csv')
        pd.DataFrame(keypoints_embeddings_for_training).to_csv('keypoints_embeddings_for_training.csv')

    # upsample to ensure embedding shapes match
    if audio_embeddings.shape[0] > keypoints_embeddings_for_training.shape[0]:
        keypoints_embeddings_for_training = resize_tensor(tensor_to_resize=keypoints_embeddings_for_training, new_length=audio_embeddings.shape[0])
    elif keypoints_embeddings_for_training.shape[0] > audio_embeddings.shape[0]:
        audio_embeddings = resize_tensor(tensor_to_resize=audio_embeddings, new_length=keypoints_embeddings_for_training.shape[0])

    # normalize and combine embeddings
    keypoints_embeddings_normalizer = DataNormalizer(keypoints_embeddings_for_training)
    normalized_keypoints_embeddings_for_training = keypoints_embeddings_normalizer.normalize_data(keypoints_embeddings_for_training)

    if run_settings.logging_settings.ENABLE_DEBUG_LOGGING:
        pd.DataFrame(normalized_keypoints_embeddings_for_training).to_csv('normalized_keypoints_embeddings_for_training.csv')

    audio_embeddings_normalizer = DataNormalizer(audio_embeddings)
    normalized_audio_embeddings_for_training = audio_embeddings_normalizer.normalize_data(audio_embeddings)

    if run_settings.logging_settings.ENABLE_DEBUG_LOGGING:
        pd.DataFrame(normalized_audio_embeddings_for_training).to_csv('normalized_audio_embeddings_for_training.csv')

    combined_embeddings = torch.cat([normalized_audio_embeddings_for_training, normalized_keypoints_embeddings_for_training], dim=0)

    if run_settings.logging_settings.ENABLE_DEBUG_LOGGING:
        pd.DataFrame(combined_embeddings).to_csv('combined_normalized_embeddings.csv')

    # train shared space projector on keypoints and rave embeddings (which exist in same-dim space)
    multimodal_projector = train_autoencoder(
        input_dim=audio_embeddings.shape[1],
        dense_dim=int(1.5 * audio_embeddings.shape[1]),
        output_dim=audio_embeddings.shape[1],
        epochs=run_settings.audio_movement_projector_settings.EPOCHS,
        batch_size=4,
        shuffle_each_epoch=True,
        enable_model_metadata_logging=run_settings.logging_settings.ENABLE_MODEL_METADATA_LOGGING,
        test_fraction=run_settings.audio_movement_projector_settings.TEST_DATA_FRACTION,
        training_data=combined_embeddings,
        model_name='shared space projector',
        output_dir_path=output_dir_path,
    )
    multimodal_projector.data_normalizer = keypoints_embeddings_normalizer

    # multimodal_projector = supervised_finetuning(
    #     model=multimodal_projector,
    #     epochs=epochs,
    #     batch_size=4,
    #     shuffle_each_epoch=False,
    #     test_fraction=0.2,
    #     training_features=normalized_keypoints_embeddings_for_training,
    #     training_labels=normalized_audio_embeddings_for_training,
    #     model_name='shared space projector (supervised finetuning)',
    # )

    # for dbg / analysis
    raw_multimodal_training_output = multimodal_projector.forward(normalized_keypoints_embeddings_for_training)
    denormalized_multimodal_training_output = keypoints_embeddings_normalizer.denormalize_data(raw_multimodal_training_output)
    print(f"multimodal_training_output shape: {denormalized_multimodal_training_output.shape}")

    if run_settings.logging_settings.ENABLE_DEBUG_LOGGING:
        pd.DataFrame(denormalized_multimodal_training_output).to_csv('denormalized_multimodal_training_output.csv')

    return AudioMovementProjector(
        audio_projector=pretrained_rave_model,
        keypoints_projector=keypoints_projector,
        multimodal_projector=multimodal_projector,
    )
