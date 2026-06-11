#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


import os
from typing import Optional

import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

from matplotlib import pyplot as plt

from src.projectors.autoencoder import AutoEncoder
from src.utils import CustomDataset


def train_autoencoder(
        input_dim: int,
        dense_dim: int,
        output_dim: int,
        epochs: int,
        batch_size: int,
        shuffle_each_epoch: bool,
        enable_model_metadata_logging: bool,
        test_fraction: float = 0,
        overfit_epochs: int = 4,
        training_data: Optional[torch.Tensor] = None,
        training_data_filename: Optional[str] = None,
        model_name: str = '',
        output_dir_path: Optional[str] = None,  # for metadata logging
) -> AutoEncoder:

    if training_data is None:
        if training_data_filename is not None:
            training_df = pd.read_csv(training_data_filename, index_col='Unnamed: 0')
            training_data = torch.tensor(training_df.to_numpy(), dtype=torch.float32)
        else:
            raise Exception("You must pass either a training_data tensor or training_data_filename str.")

    autoencoder = AutoEncoder(input_dim=input_dim, dense_dim=dense_dim, output_dim=output_dim)

    train_dataset = CustomDataset(training_data)
    train_losses = []
    if test_fraction > 0:
        train_dataset.shuffle()
        train_dataset, test_dataset = train_dataset.split(test_fraction)
        print(f"\ttrain\ttest")
        test_losses = []
    best_model_state_dict = None

    data_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=shuffle_each_epoch)

    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(autoencoder.parameters(), lr=.001)

    torch.set_grad_enabled(True)

    with tqdm(range(epochs), desc=f'Training {model_name}') as epoch_counter:
        for epoch_i in epoch_counter:
            try:
                losses = []
                for batch_i, batch_features in enumerate(data_loader):
                    optimizer.zero_grad()
                    output = autoencoder.forward(batch_features)
                    loss = loss_fn(output, batch_features)
                    loss.backward()
                    optimizer.step()
                    losses.append(loss.item())
                train_loss = np.average(losses)
                msg = f"epoch {epoch_i} avg loss: {round(train_loss, 4)}"
                train_losses.append(train_loss)
                if test_fraction > 0:
                    with torch.no_grad():
                        test_output = autoencoder.forward(test_dataset.data)
                        test_loss = loss_fn(test_output, test_dataset.data).item()
                        test_losses.append(test_loss)
                        msg += f"\t{round(test_loss, 4)}"
                        if len(test_losses) > 0 and test_loss > max(test_losses):
                            best_model_state_dict = autoencoder.state_dict()
                epoch_counter.write(msg)
                if test_fraction > 0:
                    if len(test_losses) > overfit_epochs + 1:
                        is_model_overfitting = (test_loss > train_loss) and all(test_loss > np.array(test_losses)[-(overfit_epochs + 1):-1])
                        if is_model_overfitting:
                            print("Overfit detected, stopping training")
                            break
            except KeyboardInterrupt:
                print("Training interrupted by user (KeyboardInterrupt).")
                break
    print(f'Done training {model_name}')
    if best_model_state_dict is not None:
        print(f"Restoring best model state from epoch '{np.argmax(test_losses)}'")
        autoencoder.load_state_dict(best_model_state_dict)

    if enable_model_metadata_logging:
        if output_dir_path:
            if not os.path.exists(f"{output_dir_path}/model_metadata"):
                os.mkdir(f"{output_dir_path}/model_metadata")

            if test_fraction > 0:
                train_test_losses = np.array([train_losses, test_losses]).T
                losses_names = ['train', 'test']
            else:
                train_test_losses = np.array(train_losses).T
                losses_names = ['train']

            plt.plot(range(len(train_losses)), train_test_losses)
            plt.legend(losses_names)
            plt.xlabel('epochs')
            plt.ylabel('loss')
            plt.savefig(f'{output_dir_path}/model_metadata/loss_history_{model_name}.png')
            plt.close()
        else:
            print(f"output_dir_path '{output_dir_path}' not found, skipping loss history logging for autoencoder '{model_name}'")


    torch.set_grad_enabled(False)

    return autoencoder
