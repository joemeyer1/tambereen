#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.


import os
from multiprocessing import Queue
from typing import List

import cv2
import ffmpeg
import soundfile as sf

import pandas as pd
import torch

from src.model_managers.model_file_manager import ModelFileManager
from src.projectors.movement_projector import MovementProjector
from src.streamers.draw_keypoints import draw_keypoints, draw_connections
from src.streamers.streamer_base import StreamerBase
from src.time_chunks.MovementChunk import MovementChunk
from src.time_chunks.TimeChunk import TimeChunk
from src.utils import make_name_unique


class FileWriter(StreamerBase):

    def write_files(
            self,
            file_writer_queue: Queue,
            audio_output_filename: str,
            soundless_video_output_filename: str,
            video_output_filename: str,
            draw_keypoints_to_frame: bool,
            audio_sample_rate: int,
            model_dir: str,
    ) -> None:

        time_chunks: List[TimeChunk] = file_writer_queue.get()

        if self.run_settings.logging_settings.ENABLE_AUDIO_LOGGING:
            self.write_audio_to_file(
                audio_output_filename=audio_output_filename,
                time_chunks=time_chunks,
                audio_sample_rate=audio_sample_rate,
                model_dir=model_dir,
            )
        if self.run_settings.logging_settings.ENABLE_MOVEMENT_LOGGING:
            self.write_movement_to_file(
                # movement_chunks=[time_chunk.movement_chunk for time_chunk in time_chunks],
                output_filename=soundless_video_output_filename,
                # draw_keypoints_to_frame=draw_keypoints_to_frame,
            )
        if self.run_settings.logging_settings.ENABLE_AUDIO_LOGGING and self.run_settings.logging_settings.ENABLE_MOVEMENT_LOGGING:
            self.write_audio_movement_video(
                # time_chunks=time_chunks,
                soundless_movement_video_filename=soundless_video_output_filename,
                audio_filename=audio_output_filename,
                movement_video_filename=video_output_filename,
                # chunk_time_ms=chunk_time_ms,
            )
        return

    def write_audio_to_file(self, audio_output_filename: str, time_chunks: List[TimeChunk], audio_sample_rate: int, model_dir: str) -> None:

        if not self.run_settings.audio_movement_projector_settings.PYTHON_PLAY_AUDIO:
            os.system(f"cp interfaces/out.wav {audio_output_filename.replace('.', '_mixed.')}")
            os.system(f"mv interfaces/out.wav interfaces/out0.wav")
        
        if self.run_settings.logging_settings.ENABLE_DEBUG_LOGGING:
            pd.DataFrame(torch.concatenate([time_chunk.audio_chunk.embedding_frames for time_chunk in time_chunks])).to_csv(make_name_unique(f"{model_dir}/audio_output/audio_embeddings.csv"))

        audio_movement_projector = ModelFileManager.load_model_back_compat(f"{model_dir}/model")
        if self.run_settings._is_stable_audio_3 and len(time_chunks) % 2 == 1:
            time_chunks = time_chunks[:len(time_chunks) - len(time_chunks)%2]
        if audio_movement_projector.novelifier is not None:
            novelified_embeddings = audio_movement_projector.novelifier.to('cpu').forward(torch.concatenate([time_chunk.audio_chunk.embedding_frames for time_chunk in time_chunks]).to('cpu'))
            if self.run_settings.logging_settings.ENABLE_DEBUG_LOGGING:
                pd.DataFrame(novelified_embeddings).to_csv(make_name_unique(f"{model_dir}/audio_output/novelified_audio_embeddings.csv"))
            # fmt = '\n'.join([str(novelified_embedding.shape) for novelified_embedding in novelified_embeddings])
            # print(f'dbg4398:: {novelified_embeddings.shape}')

            novelified_embeddings = novelified_embeddings.transpose(0, 1).expand(1, -1, -1)
            # print(f'dbg0398:: {novelified_embeddings.shape}')
            novelified_audio = audio_movement_projector.decode_audio_embs(novelified_embeddings.to(next(audio_movement_projector.audio_projector.parameters()).device)).detach().cpu().squeeze(0).transpose(0, 1).numpy()
            novelified_audio_output_filename = audio_output_filename.replace('.', '_novelified.')
            sf.write(make_name_unique(novelified_audio_output_filename), novelified_audio, audio_sample_rate)
        audio_embeddings = torch.cat([time_chunk.audio_chunk.embedding_frames for time_chunk in time_chunks], dim=0)
        # print(f"dbg4380: {audio_embeddings.shape}")
        audio_embeddings = audio_embeddings.transpose(0, 1).expand(1, -1, -1)
        # print(f"dbg4380: {audio_embeddings.shape}")
        audio_chunks = audio_movement_projector.decode_audio_embs(audio_embeddings.to(next(audio_movement_projector.audio_projector.parameters()).device)).detach().cpu().squeeze(0).transpose(0, 1).numpy()
        sf.write(audio_output_filename, audio_chunks, audio_sample_rate)

    def write_movement_to_file(
        self,
        # movement_chunks: List[MovementChunk],
        output_filename: str,
        # draw_keypoints_to_frame: bool,
    ):
        """Writes recorded movement to file."""

        if os.path.exists('out.mp4'):
            os.system(f"cp out.mp4 {output_filename}")
            os.system(f"mv out.mp4 out0.mp4")

        # movement_projector = MovementProjector()
        # movement_projector.load_movement_projector(audio_movement_projector_settings=self.run_settings.audio_movement_projector_settings)

        # cap = cv2.VideoCapture(0)
        # frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # cap.release()

        # audio_samples_per_audio_embedding = 2048
        # audio_samples_per_second = 44100
        # audio_embeddings_per_second = audio_samples_per_second / audio_samples_per_audio_embedding
        # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # out = cv2.VideoWriter(filename=output_filename, fourcc=fourcc, fps=audio_embeddings_per_second, frameSize=(frame_width, frame_height))
        # for movement_chunk in movement_chunks:
        #     frames = movement_chunk.frames
        #     for frame in frames:
        #         if draw_keypoints_to_frame:
        #             keypoints_with_scores = movement_projector.proj_movement_frame_to_keypoints(movement_frame=frame)
        #             # Rendering
        #             draw_connections(frame, keypoints=keypoints_with_scores)
        #             draw_keypoints(frame, keypoints=keypoints_with_scores)
        #         out.write(frame)
        # out.release()
        # cv2.destroyAllWindows()

    def write_audio_movement_video(
            self,
            # time_chunks: List[TimeChunk],
            audio_filename: str,
            movement_video_filename: str,
            soundless_movement_video_filename: str = "trash.mp4",
            # chunk_time_ms: int,
    ) -> None:
        # while not os.path.exists(movement_video_filename) or not os.path.exists(audio_filename):
        #     time.sleep(1)

        # time.sleep(5)

        # movement_duration = ffmpeg.probe(movement_video_filename)["format"]["duration"]
        # audio_duration = ffmpeg.probe(movement_video_filename)["format"]["duration"]
        # audio_offset = movement_duration - audio_duration


        print(f"cwd: {os.getcwd()}")
        p = f"{os.getcwd()}/{soundless_movement_video_filename}"
        print(f"movement_filename: {p} {os.path.exists(p)}")

        input_video = ffmpeg.input(soundless_movement_video_filename)
        input_audio = ffmpeg.input(audio_filename)  #, itsoffset=chunk_time_ms/1000)

        try:
            ffmpeg.output(input_video, input_audio, movement_video_filename).run(capture_stderr=True)
            # ffmpeg.concat(input_video, input_audio, v=1, a=1).output(movement_video_filename).run(capture_stdout=True, capture_stderr=True)
        except ffmpeg.Error as e:
            print(e.stderr.decode('utf-8'))
