
import os
import time
from multiprocessing import Queue
from typing import Optional

import cv2
import numpy as np
import torch

from src.projectors.movement_projector import MovementProjector
from src.streamers.streamer_base import StreamerBase

from src.time_chunks.MovementChunk import MovementChunk
from src.time_chunks.KeypointsChunk import KeypointsChunk
from src.time_chunks.TimeChunk import TimeChunk


class MovementStreamer(StreamerBase):

    def stream_record_movement(
        self,
        queue: Queue,
        movement_frames_per_chunk: int,
    ) -> None:
        """Record yourself dancing in front of computer and write image or keypoints data to queue."""

        load_time_start = time.time_ns()
        movement_projector = MovementProjector()
        movement_projector.load_movement_projector(audio_movement_projector_settings=self.run_settings.audio_movement_projector_settings)
        load_time_end = time.time_ns()
        print(f"stream_record_movement() loaded movement_projector in {(load_time_end - load_time_start) / 1e6} ms")

        cap = cv2.VideoCapture(0)
        cv2.startWindowThread()

        while cap.isOpened():
            try:
                chunk_time_start = time.time_ns()
                chunk_movement_frames_raw = []
                keypoints_frames_raw = []
                for frame_i in range(1, movement_frames_per_chunk + 1):
                    ret, frame = cap.read()
                    chunk_movement_frames_raw.append(frame)
                    keypoints_yx = movement_projector.proj_movement_frame_to_keypoints(movement_frame=frame)
                    keypoints_frames_raw.append(keypoints_yx)

                    cv2.imshow('MoveNet Lightning', frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        return

                chunk_movement_frames = np.array(chunk_movement_frames_raw)

                movement_chunk = MovementChunk(chunk_movement_frames)

                keypoints_frames_raw = [keypoints_frame for keypoints_frame in keypoints_frames_raw if keypoints_frame.shape[1] > 0]
                keypoints_frames = np.stack(keypoints_frames_raw)
                keypoints_chunk = KeypointsChunk(torch.tensor(keypoints_frames, dtype=torch.float32))

                time_chunk = TimeChunk(
                    movement_chunk=movement_chunk,
                    keypoints_chunk=keypoints_chunk,
                )

                queue.put(time_chunk)
                chunk_time_end = time.time_ns()
                print(f"mv->: {(chunk_time_end - chunk_time_start) / 1e6} ms")
            except KeyboardInterrupt:
                break

        cap.release()
        cv2.destroyAllWindows()


    def record_keypoints(
            self,
            max_frames: Optional[int] = None,
            output_filename: Optional[str] = None,
            show: bool = True,
            input_filename: Optional[str] = None,
    ) -> torch.Tensor:
        """Records yourself dancing in front of computer and return keypoints."""

        if max_frames is None:
            max_frames = float('inf')

        movement_projector = MovementProjector()
        movement_projector.load_movement_projector(audio_movement_projector_settings=self.run_settings.audio_movement_projector_settings)

        if input_filename is not None:
            assert os.path.exists(input_filename)
        else:
            input_filename = 0
        cap = cv2.VideoCapture(input_filename)

        cv2.startWindowThread()
        frame_i = 0
        keypoints_data = np.array([])
        frames = []
        while cap.isOpened() and frame_i < max_frames:
            ret, frame = cap.read()
            
            if not ret:
                break

            keypoints_with_scores = movement_projector.proj_movement_frame_to_keypoints(frame)
            new_keypoints_data = keypoints_with_scores

            if new_keypoints_data.shape[1] != 0:
                new_keypoints_data.reshape(1, movement_projector.pose_estimator.kp_dim * 2)
                keypoints_data = np.concatenate([keypoints_data, new_keypoints_data], axis=0) if len(keypoints_data) > 0 else new_keypoints_data

            if show:
                # Rendering
                # draw_connections(frame, keypoints=keypoints_with_scores)
                # draw_keypoints(frame, keypoints=keypoints_with_scores)
                cv2.imshow('MoveNet Lightning', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            frames.append(frame)
            frame_i += 1

        if output_filename and self.run_settings.logging_settings.ENABLE_MOVEMENT_LOGGING:
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_filename, fourcc, 20.0, (frame_width, frame_height))
            for frame in frames:
                out.write(frame)
            out.release()
        cap.release()
        cv2.destroyAllWindows()

        return torch.tensor(keypoints_data, dtype=torch.float32)
