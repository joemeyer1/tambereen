
import os
from multiprocessing import Process, Queue

from src.streamers.audio_player import AudioPlayer
from src.streamers.audio_streamer import AudioStreamer
from src.streamers.file_writer import FileWriter
from src.streamers.movement_streamer import MovementStreamer
from src.utils import make_name_unique


class AudioMovementStreamer(MovementStreamer, AudioStreamer, AudioPlayer):

    def stream_movement_to_audio(
            self,
            model_dir: str,
            python_play_audio: bool = False,
            audio_frames_per_chunk: int = 1,
            tambereen_interface_path: str = 'interfaces/tambereen_interface_percussion.maxpat'
    ):
        
        if not python_play_audio:
            os.system(f"open {tambereen_interface_path}")

        output_movement_dir = f"{model_dir}/movement_output"
        if not os.path.exists(output_movement_dir):
            os.mkdir(output_movement_dir)
        output_movement_filename = make_name_unique(f"{output_movement_dir}/interact_movement.mp4")

        soundless_output_movement_dir = f"{model_dir}/soundless_movement_output"
        if not os.path.exists(soundless_output_movement_dir):
            os.mkdir(soundless_output_movement_dir)
        soundless_output_movement_filename = make_name_unique(f"{soundless_output_movement_dir}/interact_movement.mp4")

        output_audio_dir = f"{model_dir}/audio_output"
        if not os.path.exists(output_audio_dir):
            os.mkdir(output_audio_dir)
        output_audio_filename = make_name_unique(f"{output_audio_dir}/interact_movement_to_audio.wav")

        movement_frames_per_chunk = audio_frames_per_chunk
        print(f"movement_frames_per_chunk: {movement_frames_per_chunk}")
        print(f"audio_frames_per_chunk: {audio_frames_per_chunk}")

        movement_queue = Queue()
        audio_queue = Queue()

        stream_movement_proc = Process(target=self.stream_record_movement, args=(movement_queue, movement_frames_per_chunk))
        stream_map_audio_proc = Process(target=self.stream_audio_embs_from_movement, args=(movement_queue, audio_queue, model_dir, python_play_audio))

        if python_play_audio:
            print(f"python_play_audio: {python_play_audio}")
            stream_play_audio_proc = Process(target=self.play_audio_stream, args=(audio_queue, model_dir))

        stream_movement_proc.start()
        stream_map_audio_proc.start()
        if python_play_audio:
            stream_play_audio_proc.start()

        try:
            stream_movement_proc.join()
            stream_map_audio_proc.join()
            if python_play_audio:
                stream_play_audio_proc.join()
        except KeyboardInterrupt:
            if self.run_settings.logging_settings.ENABLE_AUDIO_LOGGING or self.run_settings.logging_settings.ENABLE_MOVEMENT_LOGGING:
                print(f"\nwriting files...")
                FileWriter(run_settings=self.run_settings).write_files(
                    file_writer_queue=audio_queue,  # file_writer_queue
                    audio_output_filename=output_audio_filename,
                    soundless_video_output_filename=soundless_output_movement_filename,
                    video_output_filename=output_movement_filename,
                    draw_keypoints_to_frame=False,
                    audio_sample_rate=44100,
                    model_dir=model_dir,
                )
                print("done")
            stream_movement_proc.terminate()
            stream_map_audio_proc.terminate()
            if python_play_audio:
                stream_play_audio_proc.terminate()

    # @staticmethod
    # def _get_audio_embeddings_per_second(
    #         model_dir: str,
    #         test_file: str = "audio_training_data/percussion/banana-shaker__long_forte_shaken.wav",
    # ) -> int:
    #     """Returns the number of audio embeddings associated with a second of audio."""

    #     AUDIO_FRAMES_PER_RAVE_FRAME = 2048
    #     AUDIO_FRAMES_PER_SEC = 44100

    #     rave_frames_per_audio_frame = 1 / AUDIO_FRAMES_PER_RAVE_FRAME
    #     rave_frames_per_sec = rave_frames_per_audio_frame * AUDIO_FRAMES_PER_SEC
    #     assert rave_frames_per_sec == 21.533203125


    #     data, sr = sf.read(test_file, dtype='float32')

    #     audio_movement_projector = ModelFileManager.load_model_back_compat(f"{model_dir}/model")
    #     audio_embeddings_per_second = len(audio_movement_projector.embed_audio(data[:sr]))
    #     return audio_embeddings_per_second

    # def _get_movement_frames_per_second(self, test_secs: int = 10) -> int:
    #     return 29

    #     cap = cv2.VideoCapture(0)
    #     cv2.startWindowThread()

    #     frames_i = 0

    #     test_nanosecs = test_secs * 1e9

    #     st = time.time_ns()

    #     while time.time_ns() - st <= test_nanosecs:
    #         ret, frame = cap.read()
    #         cv2.imshow('MoveNet Lightning', frame)
    #         cv2.waitKey(1)
    #         frames_i += 1
    #     cap.release()
    #     cv2.destroyAllWindows()
    #     movement_frames_per_second = ceil(frames_i / test_secs)
    #     return int(movement_frames_per_second)
