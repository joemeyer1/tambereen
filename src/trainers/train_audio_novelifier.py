#!/usr/bin/env python3
# Copyright (c) 2024 Joseph Meyer. All Rights Reserved.


import os
from typing import Any, Callable, List, Optional, Tuple, Dict

import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import soundfile as sf
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

from src.model_managers.rave_loader import RaveLoader
from src.projectors.audio_movement_projector import AudioMovementProjector
from src.projectors.novelifier import Novelifier
from src.trainers._embeddings_assessor import EmbeddingsAssessor
from src.utils import get_audio_data, make_name_unique, CustomDataset

from run_settings import RunSettings


def train_audio_novelifier(
        run_settings: RunSettings,
        batch_size: int,
        shuffle_each_epoch: bool,
        output_dir_path: str,
) -> Novelifier:

    # GET MAX AUDIO FRAMES / EMBEDDINGS
    max_audio_secs = run_settings.audio_novelifier_settings.MAX_AUDIO_SECS
    if max_audio_secs is not None and max_audio_secs > 0:
        samples_per_sec = 44100
        max_audio_frames = int(max_audio_secs * samples_per_sec)

        samples_per_embedding = 2048
        embeddings_per_sec = samples_per_sec / samples_per_embedding
        max_audio_embeddings = int(max_audio_secs * embeddings_per_sec)
    else:
        max_audio_frames = None
        max_audio_embeddings = None

    # rave_model_name, audio_dir_paths = 'percussion', 'audio_training_data/percussion'
    # rave_model_name, audio_dir_paths = 'musicnet', 'audio_training_data/violin'
    rave_model_name, audio_dir_paths = run_settings.RAVE_MODEL,  run_settings.audio_novelifier_settings.AUDIO_TRAINING_DATA_PATH

    pretrained_rave_model = RaveLoader().download_official_model_by_name(model_name=run_settings.RAVE_MODEL)

    # MAKE DATASET
    audio_embeddings_cache_path = f"{'/'.join(audio_dir_paths.split('/')[:-1])}/_cached_embeddings/" \
                                  f"{audio_dir_paths.split('/')[-1]}.pt"
    if run_settings.audio_novelifier_settings.USE_CACHE and os.path.exists(audio_embeddings_cache_path):
        print(f"Loading cached audio embeddings...")
        audio_embeddings = torch.load(audio_embeddings_cache_path)
        if max_audio_embeddings is not None:
            audio_embeddings = audio_embeddings[:max_audio_embeddings]
    else:
        audio_data, audio_sample_rate = get_audio_data(audio_dir_paths=audio_dir_paths, max_audio_frames=max_audio_frames)

        if len(audio_data.shape) > 1:  # convert to mono
            audio_data = audio_data.mean(1)

        # encode audio
        audio_embeddings = AudioMovementProjector(audio_projector=pretrained_rave_model).embed_audio(audio_data)
        print(f"Caching audio embeddings...")
        if not os.path.exists(f"{'/'.join(audio_embeddings_cache_path.split('/')[:-1])}"):
            os.mkdir(f"{'/'.join(audio_embeddings_cache_path.split('/')[:-1])}")
        torch.save(audio_embeddings, audio_embeddings_cache_path)

    audio_embeddings = audio_embeddings[torch.randperm(audio_embeddings.shape[0])]  # shuffle audio embeddings
    rand_perm_audio_embeddings = audio_embeddings[torch.randperm(audio_embeddings.shape[0])]  # new shuffle for reference
    print(f"dataset shape: ({audio_embeddings.shape}, {rand_perm_audio_embeddings.shape})")
    audio_embeddings_dataset = CustomDataset(audio_embeddings, metadata=rand_perm_audio_embeddings)  # , metadata=pretrained_rave_model.decode(audio_embeddings).expand(1, -1, -1)).reshape(-1))
    if run_settings.audio_novelifier_settings.TEST_DATA_FRACTION > 0:
        train_data, test_data = audio_embeddings_dataset.split(run_settings.audio_novelifier_settings.TEST_DATA_FRACTION)
    else:
        train_data, test_data = audio_embeddings_dataset, None
    data_loader = DataLoader(train_data, batch_size=batch_size, shuffle=shuffle_each_epoch)

    # TRAIN
    novelifier_trainer = NovelifierTrainer(pretrained_rave_model=pretrained_rave_model, output_dir_path=output_dir_path, run_settings=run_settings)
    novelifier = novelifier_trainer.train_novelifier(
        latent_dim=audio_embeddings.shape[1],
        dense_dim=audio_embeddings.shape[1],
        data_loader=data_loader,
        epochs=run_settings.audio_novelifier_settings.EPOCHS,
        test_data=test_data,
    )
    return novelifier


class NovelifierTrainer(EmbeddingsAssessor):
    output_dir_path: str
    run_settings: RunSettings

    def __init__(self, pretrained_rave_model, output_dir_path: str, run_settings: RunSettings, instability_tolerance: float = 1.2):
        EmbeddingsAssessor.__init__(self, instability_tolerance=instability_tolerance)
        self.pretrained_rave_model = pretrained_rave_model
        self.run_settings = run_settings
        self.output_dir_path = output_dir_path

    def train_novelifier(self, latent_dim: int, dense_dim: int, data_loader: DataLoader, epochs: int = 200, test_data: Optional[CustomDataset] = None) -> Novelifier:

        novelifier = Novelifier(latent_dim=latent_dim, dense_dim=dense_dim, submodule_names=['divergence', 'stability'])
        super_optimizer = torch.optim.Adam(novelifier.parameters(), lr=.001, maximize=True)

        divergence_module = novelifier.submodules['divergence']
        divergence_optimizer = torch.optim.Adam(divergence_module.parameters(), lr=.001, maximize=True)

        stability_module = novelifier.submodules['stability']
        stability_optimizer = torch.optim.Adam(stability_module.parameters(), lr=.001, maximize=True)

        name_to_optim_objective = {
            'divergence': (divergence_optimizer, self.assess_divergence),
            'stability': (stability_optimizer, self.assess_stability),
            None: (super_optimizer, self.assess_transformed_embeddings)
        }
        self._train_modules(
            novelifier=novelifier,
            name_to_optim_objective=name_to_optim_objective,
            epochs=epochs,
            data_loader=data_loader,
            test_data=test_data,
        )
        return novelifier

    def train_simple_novelifier(self, latent_dim: int, dense_dim: int, data_loader: DataLoader, epochs: int = 200, test_data: Optional[CustomDataset] = None) -> Novelifier:

        novelifier = Novelifier(latent_dim=latent_dim, dense_dim=dense_dim)
        super_optimizer = torch.optim.Adam(novelifier.parameters(), lr=.001, maximize=True)

        name_to_optim_objective = {
            None: (super_optimizer, self.assess_transformed_embeddings)
        }
        self._train_modules(
            novelifier=novelifier,
            name_to_optim_objective=name_to_optim_objective,
            epochs=epochs,
            data_loader=data_loader,
            test_data=test_data,
        )
        return novelifier

    def _train_modules(
        self,
        novelifier: Novelifier,
        name_to_optim_objective: Dict[Optional[str], Tuple[Any, Callable]],
        epochs: int,
        data_loader: DataLoader,
        overfit_epochs: int = 4,  # stop training after n epochs overfit
        test_data: Optional[CustomDataset] = None,
    ):

        torch.set_grad_enabled(True)
        submodule_name_to_rewards: Dict[str, List[float]] = {name: [] for name in name_to_optim_objective}
        reward_labels = '\t' + '\t'.join([str(name) for name in name_to_optim_objective.keys()]).replace('None', 'total')
        if test_data is not None:
            reward_labels += '\t' + 'test'
            submodule_name_to_rewards['test'] = []
        print(reward_labels)
        evolving_novelified_audio: List[np.ndarray] = []
        best_model_state_dict = None
        with tqdm(range(epochs), desc=f'Training Modules') as epoch_counter:

            for epoch_i in epoch_counter:
                try:
                    submodule_name_to_epoch_rewards: Dict[str, List[float]] = {name: [] for name in name_to_optim_objective}
                    for batch_i, (batch_embeddings, batch_embeddings_ref) in enumerate(data_loader):
                        for (submodule_name, (optimizer, objective)) in name_to_optim_objective.items():
                            optimizer.zero_grad()
                            batch_reward = self._compute_objective(
                                embeddings_original=batch_embeddings,
                                embeddings_ref=batch_embeddings_ref,
                                novelifier=novelifier,
                                objective=objective,
                                submodule_name=submodule_name,
                            )
                            batch_reward.backward()
                            optimizer.step()
                            submodule_name_to_epoch_rewards[submodule_name].append(batch_reward.item())

                    epoch_rewards_msg = f"epoch {epoch_i} avg rewards: " + ''.join(f"{round(np.average(rewards), 4)}\t" for rewards in submodule_name_to_epoch_rewards.values())

                    with torch.no_grad():
                        if test_data is not None:
                            test_reward = self._compute_objective(
                                embeddings_original=test_data.data,
                                embeddings_ref=test_data.metadata,
                                novelifier=novelifier,
                                objective=self.assess_transformed_embeddings,
                                evolving_novelified_audio=evolving_novelified_audio,
                            )
                            if len(submodule_name_to_rewards['test']) > 0 and test_reward > max(submodule_name_to_rewards['test']):
                                best_model_state_dict = novelifier.state_dict()
                            submodule_name_to_rewards['test'].append(round(test_reward.item(), 4))
                            epoch_rewards_msg += f"{round(test_reward.item(), 4)}"

                        epoch_counter.write(epoch_rewards_msg)
                        for submodule_name, epoch_rewards in submodule_name_to_epoch_rewards.items():
                            submodule_name_to_rewards[submodule_name].append(round(np.average(epoch_rewards), 4))

                        if test_data is not None:
                            if len(submodule_name_to_rewards['test']) > overfit_epochs + 1:
                                is_model_overfitting = (test_reward < submodule_name_to_rewards[None][-1]) and all(test_reward < prior_reward for prior_reward in submodule_name_to_rewards['test'][-(overfit_epochs + 1):-1])
                                if is_model_overfitting:
                                    print("Overfit detected, stopping training")
                                    break

                except KeyboardInterrupt:
                    print("Training interrupted by user (KeyboardInterrupt).")
                    break
            torch.set_grad_enabled(False)
            print(f'Done training submodules {name_to_optim_objective.keys()}')
            if best_model_state_dict is not None:
                print(f"Restoring best model state from epoch '{np.argmax(submodule_name_to_rewards['test'])}'")
                novelifier.load_state_dict(best_model_state_dict)

            if self.run_settings.logging_settings.ENABLE_MODEL_METADATA_LOGGING:
                if not os.path.exists(f"{self.output_dir_path}/model_metadata"):
                    os.mkdir(f"{self.output_dir_path}/model_metadata")

                plt.plot(range(len(list(submodule_name_to_rewards.values())[0])), np.array(list(submodule_name_to_rewards.values())).T)
                plt.legend([str(k).replace('None', 'total') for k in submodule_name_to_rewards.keys()])
                plt.xlabel('epochs')
                plt.ylabel('reward')
                plt.savefig(f'{self.output_dir_path}/model_metadata/reward_history_novelifier.png')
                plt.close()

            if self.run_settings.logging_settings.ENABLE_AUDIO_LOGGING:
                novelified_audio_over_training_dir = make_name_unique(f"{self.output_dir_path}/novelified_audio_over_training")
                os.mkdir(novelified_audio_over_training_dir)
                for epoch_audio in evolving_novelified_audio:
                    sf.write(make_name_unique(f'{novelified_audio_over_training_dir}/epoch.wav'), data=epoch_audio, samplerate=44100)
                sf.write(make_name_unique(f'{novelified_audio_over_training_dir}/full_evolving_novelified_audio.wav'), data=np.concatenate(evolving_novelified_audio), samplerate=44100)

    def _compute_objective(
            self,
            embeddings_original: torch.Tensor,
            embeddings_ref: torch.Tensor,
            novelifier: Novelifier,
            objective: Callable,
            submodule_name: Optional[str] = None,
            evolving_novelified_audio: Optional[List[np.ndarray]] = None,
    ) -> torch.Tensor:

        embeddings_transformed = novelifier.forward(embeddings_original, submodule_name=submodule_name)

        embeddings_ref_transformed = novelifier.forward(embeddings_ref)

        with torch.no_grad():
            embeddings_transformed_formatted = embeddings_transformed.transpose(0, 1).expand(1, -1, -1)
            novelified_audio = self.pretrained_rave_model.decode(embeddings_transformed_formatted)
            if novelified_audio.shape[1] > 1:  # convert to mono
                novelified_audio = novelified_audio.mean(1).expand(1, -1, -1)

            if evolving_novelified_audio is not None:
                novelifed_audio_np = novelified_audio.reshape(-1).numpy()
                evolving_novelified_audio.append(novelifed_audio_np)
                if not self.run_settings.audio_novelifier_settings.MUTE_DURING_TRAINING:
                    sd.play(novelifed_audio_np, samplerate=44100)

            embeddings_transformed_prime = self.pretrained_rave_model.encode(novelified_audio)
            embeddings_silence = self.pretrained_rave_model.encode(torch.zeros_like(novelified_audio))

        reward = objective(
            embeddings_original=embeddings_original,  # embeddings before transformation,
            embeddings_silence=embeddings_silence,  # projection of silence into latent space
            embeddings_transformed=embeddings_transformed,
            # embeddings_transformed_formatted=embeddings_transformed_formatted,
            embeddings_transformed_prime=embeddings_transformed_prime,
            embeddings_ref=embeddings_ref,
            embeddings_ref_transformed=embeddings_ref_transformed,
        )
        return reward
