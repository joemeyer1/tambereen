
import os
from typing import Optional

import ffmpeg
import numpy as np

from src.model_managers.model_file_manager import ModelFileManager
from src.projectors.audio_movement_projector import AudioMovementProjector
from src.projectors.data_normalizer import DataNormalizer
from src.streamers.movement_streamer import MovementStreamer
from src.trainers.finetune import finetune
from src.utils import resize_tensor


def supervised_finetune_audio_movement_projector(model_dirname: str, training_data_filename: str, epochs: int, max_movement_frames: Optional[int]) -> AudioMovementProjector:

    model_path = f"{model_dirname}/model"
    assert os.path.exists(training_data_filename)
    assert os.path.exists(model_path)

    audio_movement_projector = ModelFileManager.load_model(model_path)

    # Read raw PCM audio from MP4 via ffmpeg-python; line below was re-written starting from Claude suggestion
    out, _ = (
        ffmpeg
        .input(training_data_filename)
        .output('pipe:', format='f32le', acodec='pcm_f32le', ar=44100, ac=1)
        .run(capture_stdout=True, quiet=True)
    )
    audio_data = np.frombuffer(out, dtype=np.float32)

    # audio_input_filename = input_filename.replace('.mp4', '.wav')
    # # audio_stream = ffmpeg.input(input_filename).audio
    # # ffmpeg.output(audio_stream, audio_input_filename).run(capture_stderr=True)
    # audio_data, audio_sample_rate = sf.read(audio_input_filename, dtype='float32')
    audio_embeddings = audio_movement_projector.embed_audio(audio_data)

    keypoints_data_for_training = MovementStreamer().record_keypoints(
        max_frames=max_movement_frames,
        input_filename=training_data_filename,
        show=False,
        # output_filename=f"{output_dir_path}/movement_training_data.mp4",
    )
    keypoints_embeddings_for_training = audio_movement_projector.encode_keypoints(keypoints_data=keypoints_data_for_training)
    
    # upsample to ensure embedding shapes match
    if audio_embeddings.shape[0] > keypoints_embeddings_for_training.shape[0]:
        keypoints_embeddings_for_training = resize_tensor(tensor_to_resize=keypoints_embeddings_for_training, new_length=audio_embeddings.shape[0])
    elif keypoints_embeddings_for_training.shape[0] > audio_embeddings.shape[0]:
        audio_embeddings = resize_tensor(tensor_to_resize=audio_embeddings, new_length=keypoints_embeddings_for_training.shape[0])

    # normalize and combine embeddings
    keypoints_embeddings_normalizer = DataNormalizer(keypoints_embeddings_for_training)
    normalized_keypoints_embeddings_for_training = keypoints_embeddings_normalizer.normalize_data(keypoints_embeddings_for_training)
    # pd.DataFrame(normalized_keypoints_embeddings_for_training).to_csv('normalized_keypoints_embeddings_for_training.csv')  # for debugging

    audio_embeddings_normalizer = DataNormalizer(audio_embeddings)
    normalized_audio_embeddings_for_training = audio_embeddings_normalizer.normalize_data(audio_embeddings)
    # pd.DataFrame(normalized_audio_embeddings_for_training).to_csv('normalized_audio_embeddings_for_training.csv')  # for debugging

    # combined_embeddings = torch.cat([normalized_audio_embeddings_for_training, normalized_keypoints_embeddings_for_training], dim=0)
    # pd.DataFrame(combined_embeddings).to_csv('combined_normalized_embeddings.csv')

    audio_movement_projector.multimodal_projector = finetune(
        model=audio_movement_projector.multimodal_projector,
        epochs=epochs,
        batch_size=4,
        shuffle_each_epoch=False,
        test_fraction=0.2,
        training_features=normalized_keypoints_embeddings_for_training,
        training_labels=normalized_audio_embeddings_for_training,
        model_name='shared space projector (supervised finetuning)',
    )

    return audio_movement_projector
