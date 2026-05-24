

from src.model_managers.model_file_manager import ModelFileManager
from src.projectors.audio_movement_projector import AudioMovementProjector


def test_load_model(model_path: str = 'output_data_runs/0/model/') -> AudioMovementProjector:
    model = ModelFileManager.load_model_back_compat(model_path)
    print(model)
    return model


if __name__ == '__main__':
    test_load_model()
