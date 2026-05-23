#!/usr/bin/env python3
# Copyright (c) 2024 Joseph Meyer. All Rights Reserved.


import pandas as pd

from src.streamers.movement_streamer import MovementStreamer
from src.trainers.train_autoencoder import train_autoencoder
from src.projectors.audio_movement_projector import AudioMovementProjector
from src.projectors.data_normalizer import DataNormalizer



def test_keypoints_encoder(epochs: int, max_frames: int):
    # extract keypoints (e.g. with MoveNet) to train keypoints encoder on
    keypoints_data_for_training = MovementStreamer().record_keypoints(max_frames=max_frames)
    pd.DataFrame(keypoints_data_for_training).to_csv("keypoints_data_for_training.csv")

    keypoints_normalizer = DataNormalizer(keypoints_data_for_training)
    normalized_keypoints_data_for_training = keypoints_normalizer.normalize_data(keypoints_data_for_training)
    pd.DataFrame(normalized_keypoints_data_for_training).to_csv('normalized_keypoints_data_for_training.csv')  # for debugging


    # train encoder to project keypoints into a latent space of same dimension as RAVE's latent space (e.g. "4")
    keypoints_encoder = train_autoencoder(
        input_dim=17 * 2,
        dense_dim=16,
        output_dim=4,
        training_data=keypoints_data_for_training,
        epochs=epochs,
        model_name='keypoints encoder',
        shuffle_each_epoch=True,
        batch_size=1,
        test_fraction=0,
        enable_model_metadata_logging=False,
    )
    movement_to_sound_generator = AudioMovementProjector(keypoints_projector=keypoints_encoder)
    keypoints_embeddings = movement_to_sound_generator.encode_keypoints(keypoints_data=keypoints_data_for_training)
    print(f"keypoints_embeddings: {keypoints_embeddings}")
    print(f"keypoints_embeddings.shape: {keypoints_embeddings.shape}")


if __name__ == '__main__':
    test_keypoints_encoder(epochs=10, max_frames=25)
