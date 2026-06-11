

import os
from typing import Optional

import torch

from src.projectors.audio_movement_projector import AudioMovementProjector
from run_settings import RunSettings

torch.set_grad_enabled(False)


class ModelFileManager:

    @staticmethod
    def save_model(audio_movement_projector: AudioMovementProjector, output_dir_name: str) -> None:

        if not os.path.exists(output_dir_name):
            os.mkdir(output_dir_name)

        if audio_movement_projector.keypoints_projector is not None:
            torch.save(audio_movement_projector.keypoints_projector, f'{output_dir_name}/keypoints_projector.pt')
        if audio_movement_projector.multimodal_projector is not None:
            torch.save(audio_movement_projector.multimodal_projector, f'{output_dir_name}/shared_latent_space_projector.pt')
        if audio_movement_projector.audio_projector is not None:
            torch.jit.save(audio_movement_projector.audio_projector, f'{output_dir_name}/audio_projector.ts')
        if audio_movement_projector.novelifier is not None:
            torch.save(audio_movement_projector.novelifier, f'{output_dir_name}/audio_novelifier.pt')

    @staticmethod
    def load_model_back_compat(output_dir_name) -> AudioMovementProjector:
        """Backwards compatible load_model() fn."""

        print(f"loading model from {output_dir_name}")

        audio_movement_projector = AudioMovementProjector()

        if os.path.exists(f'{output_dir_name}/keypoints_projector.pt'):
            audio_movement_projector.keypoints_projector = torch.load(f'{output_dir_name}/keypoints_projector.pt')

        if os.path.exists(f'{output_dir_name}/shared_latent_space_projector.pt'):
            audio_movement_projector.multimodal_projector = torch.load(f'{output_dir_name}/shared_latent_space_projector.pt')
        elif os.path.exists(f'{output_dir_name}/audio_movement_projector.pt'):  # legacy
            audio_movement_projector.multimodal_projector = torch.load(f'{output_dir_name}/audio_movement_projector.pt')

        if os.path.exists(f'{output_dir_name}/audio_projector.ts'):
            audio_movement_projector.audio_projector = torch.load(f'{output_dir_name}/audio_projector.ts')
        elif os.path.exists(f'{output_dir_name}/audio_autoencoder.ts'):  # legacy
            audio_movement_projector.audio_projector = torch.load(f'{output_dir_name}/audio_autoencoder.ts')

        novelifier_path = f'{output_dir_name}/audio_novelifier.pt'
        if os.path.exists(novelifier_path):
            audio_movement_projector.novelifier = torch.load(novelifier_path)

        return audio_movement_projector

    @staticmethod
    def load_model(output_dir_name) -> AudioMovementProjector:
        audio_movement_projector = AudioMovementProjector()

        keypoints_projector_path = f'{output_dir_name}/keypoints_projector.pt'
        if os.path.exists(keypoints_projector_path):
            audio_movement_projector.keypoints_projector = torch.load(keypoints_projector_path)

        shared_latent_space_projector = f'{output_dir_name}/shared_latent_space_projector.pt'
        if os.path.exists(shared_latent_space_projector):
            audio_movement_projector.multimodal_projector = torch.load(shared_latent_space_projector)

        audio_projector_path = f'{output_dir_name}/audio_projector.ts'
        if os.path.exists(audio_projector_path):
            audio_movement_projector.audio_projector = torch.load(audio_projector_path)

        novelifier_path = f'{output_dir_name}/audio_novelifier.pt'
        if os.path.exists(novelifier_path):
            audio_movement_projector.novelifier = torch.load(novelifier_path)

        return audio_movement_projector


    @staticmethod
    def load_model_legacy(output_dir_name) -> AudioMovementProjector:
        """Deprecated, but use for loading older models."""
        
        audio_movement_projector = AudioMovementProjector()

        keypoints_projector_path = f'{output_dir_name}/keypoints_projector.pt'
        if os.path.exists(keypoints_projector_path):
            audio_movement_projector.keypoints_projector = torch.load(keypoints_projector_path)

        shared_latent_space_projector = f'{output_dir_name}/audio_movement_projector.pt'
        if os.path.exists(shared_latent_space_projector):
            audio_movement_projector.multimodal_projector = torch.load(shared_latent_space_projector)

        audio_projector_path = f'{output_dir_name}/audio_autoencoder.ts'
        if os.path.exists(audio_projector_path):
            audio_movement_projector.audio_projector = torch.load(audio_projector_path)

        return audio_movement_projector

    @staticmethod
    def does_pretrained_model_exist(pretrained_model_path: Optional[str], submodule_path: str):
        if pretrained_model_path is None:
            return False
        elif not os.path.exists(f"{pretrained_model_path}/model/{submodule_path}"):
            return False
        else:
            return True
        
    def are_all_models_pretrained_in_unified_folder(self, run_settings: RunSettings):
        if not self.does_pretrained_model_exist(
            pretrained_model_path=run_settings.audio_movement_projector_settings.PRETRAINED_MODEL_PATH,
            submodule_path='shared_latent_space_projector.pt',
        ):
            return False
        elif not self.does_pretrained_model_exist(
            pretrained_model_path=run_settings.audio_novelifier_settings.PRETRAINED_MODEL_PATH,
            submodule_path='audio_novelifier.pt',
        ):
            return False
        elif run_settings.audio_movement_projector_settings.PRETRAINED_MODEL_PATH != run_settings.audio_novelifier_settings.PRETRAINED_MODEL_PATH:
            return False
        else:  # both models exist pre-trained in unified folder
            return True
