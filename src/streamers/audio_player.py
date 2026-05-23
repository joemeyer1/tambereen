import time
from multiprocessing import Queue
from typing import List

import sounddevice as sd

from src.model_managers.model_file_manager import ModelFileManager
from src.time_chunks.TimeChunk import TimeChunk


class AudioPlayer:

    @staticmethod
    def play_audio_stream(
            audio_queue: Queue,
            model_dir: str,
            audio_sample_rate: int = 44100,
    ) -> List[TimeChunk]:
        """Reads audio embeddings stream from queue, decodes it to audio, and plays it directly via Python.
        
        This function is typically not used; playing audio directly via Python is slow and sounds glitchy during real-time interaction (though not in recordings). But this method is here for cases where Max MSP patch is not available. Note that novelified audio mixing is only available when streaming to the Max patch, not when playing audio directly in python (which has no mechanism for interactive interpolation).
        """

        audio_movement_projector = ModelFileManager.load_model_back_compat(f"{model_dir}/model")

        time_chunks = []
        while True:
            try:
                start_time = time.time_ns()
                time_chunk: TimeChunk = audio_queue.get()

                if time_chunk.audio_chunk.wav_data is None:
                    time_chunk.audio_chunk.wav_data = audio_movement_projector.decode_audio_embs(time_chunk.audio_chunk.embedding_frames.expand(1, -1, -1).transpose(1, 2)).flatten().numpy()
                    sd.play(time_chunk.audio_chunk.wav_data, samplerate=audio_sample_rate)
                end_time = time.time_ns()
                print(f"play() in {(end_time - start_time) / 1e6} ms\n")
                time_chunks.append(time_chunk)

            except KeyboardInterrupt:
                audio_queue.put(time_chunks)
                return time_chunks
