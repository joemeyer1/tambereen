#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. All Rights Reserved.


import time
from multiprocessing import Queue

import sounddevice as sd

from src.model_managers.model_file_manager import ModelFileManager
from src.streamers.streamer_base import StreamerBase
from src.time_chunks.TimeChunk import TimeChunk


class AudioStreamer(StreamerBase):

    def stream_audio_embs_from_movement(
            self,
            keypoints_queue: Queue,
            audio_queue: Queue,
            model_dir: str,
            python_play_audio: bool = False,
    ) -> None:
        """Reads movement stream from queue, decodes it to audio and passes to output queue upon interrupt."""

        model_load_time_start = time.time_ns()
        audio_movement_projector = ModelFileManager.load_model_back_compat(f"{model_dir}/model")
        audio_movement_projector.load_movement_projector(audio_movement_projector_settings=self.run_settings.audio_movement_projector_settings)
        model_load_time_end = time.time_ns()
        print(f"stream_audio_embs_from_movement() loaded audio_movement_projector in {(model_load_time_end - model_load_time_start) / 1e6} ms")

        time_chunks = []
        while True:
            try:
                start_time = time.time_ns()
                time_chunk: TimeChunk = keypoints_queue.get()

                if time_chunk.keypoints_chunk is None:
                    time_chunk.keypoints_chunk = audio_movement_projector.proj_movement_chunk_to_keypoints(movement_chunk=time_chunk.movement_chunk)
                time_chunk.audio_chunk = audio_movement_projector.proj_keypoints_to_audio_embs(keypoints_chunk=time_chunk.keypoints_chunk, osc_stream_audio=not python_play_audio)

                sd.wait()
                time_chunks.append(time_chunk)

                if python_play_audio:
                    audio_queue.put(time_chunk)
                    
                end_time = time.time_ns()
                print(f"->au: {(end_time - start_time) / 1e6} ms")


            except KeyboardInterrupt:
                if not python_play_audio:
                    audio_queue.put(time_chunks)
                return
