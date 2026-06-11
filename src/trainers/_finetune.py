from typing import Optional

import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

from src.utils import CustomDataset


def finetune(
        model: torch.nn.Module,
        epochs: int,
        batch_size: int,
        shuffle_each_epoch: bool,
        test_fraction: float = 0,
        overfit_epochs: int = 4,
        training_features: Optional[torch.Tensor] = None,
        training_labels: Optional[torch.Tensor] = None,
        training_data_filename: Optional[str] = None,
        model_name: str = '',
) -> torch.nn.Module:
    """Helper function for supervised_finetune_audio_movement_projector."""

    if training_features is None:
        if training_data_filename is not None:
            training_df = pd.read_csv(training_data_filename, index_col='Unnamed: 0')
            training_features = torch.tensor(training_df.to_numpy(), dtype=torch.float32)
        else:
            raise Exception("You must pass either a training_data tensor or training_data_filename str.")

    train_dataset = CustomDataset(training_features, metadata=training_labels)
    if test_fraction > 0:
        train_dataset.shuffle()
        train_dataset, test_dataset = train_dataset.split(test_fraction)
        print(f"\ttrain\ttest")
        test_losses = []
    best_model_state_dict = None

    data_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=shuffle_each_epoch)

    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)

    torch.set_grad_enabled(True)

    with tqdm(range(epochs), desc=f'Training {model_name}') as epoch_counter:
        for epoch_i in epoch_counter:
            try:
                losses = []
                for batch_i, batch in enumerate(data_loader):
                    if training_labels is None:  # unsupervised
                        batch_features = batch
                        batch_labels = batch
                    else:  # supervised
                        batch_features, batch_labels = batch

                    optimizer.zero_grad()
                    output = model.forward(batch_features)
                    loss = loss_fn(output, batch_labels)
                    loss.backward()
                    optimizer.step()
                    losses.append(loss.item())
                train_loss = np.average(losses)
                msg = f"epoch {epoch_i} avg loss: {round(train_loss, 4)}"
                if test_fraction > 0:
                    with torch.no_grad():
                        test_features = test_dataset.data
                        test_labels = test_dataset.data if training_labels is None else test_dataset.metadata
                        test_output = model.forward(test_features)
                        test_loss = loss_fn(test_output, test_labels).item()
                        test_losses.append(test_loss)
                        msg += f"\t{round(test_loss, 4)}"
                        if len(test_losses) > 0 and test_loss > max(test_losses):
                            best_model_state_dict = model.state_dict()
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
        model.load_state_dict(best_model_state_dict)

    torch.set_grad_enabled(False)

    return model
