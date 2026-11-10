

from time import time_ns

import torch

from src.model_managers.audio_model_loader import AudioModelLoader

torch.set_grad_enabled(False)


def benchmark_decoding(iters: int = 1000):
    """Returns time (ms) per embedding decoding."""

    audio_projector = AudioModelLoader().load_model('percussion')
    embeddings = torch.randn(iters, 4)

    start = time_ns()
    for embedding in embeddings:
        decoded_audio = audio_projector.decode(embedding.expand(1, 1, -1)).numpy()
    end = time_ns()
    decode_time = (end - start) / (iters * 1e6)
    print(f"{decode_time} ms per embedding decode call")
    return decode_time
