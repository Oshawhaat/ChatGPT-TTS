from TTS.api import TTS
import simpleaudio
import threading
import os


def _play_stack():
        count = 0
        while True: 
                while not f"output{count}.wav" in message_stack:
                        pass

                play_sound_file(message_stack.pop())
                count += 1

tts = TTS(model_name="tts_models/en/jenny/jenny")

message_stack = []

sound_thread = threading.Thread(target=_play_stack)
sound_thread.start()


def text_to_file(args: tuple) -> str:
        count, text = args
        path = f"output{count}.wav"
        tts.tts_to_file(text=text, file_path=path)

        print("Created sound file: " + path)

        return path

def play_sound_file(path) -> None:
        print("started playing: " + path)
        wave_obj = simpleaudio.WaveObject.from_wave_file(path)
        play_obj = wave_obj.play()
        play_obj.wait_done()
        os.remove(path)
        print("done playing: " + path)

def add_to_stack(text: str):
        path = text_to_file(text)

        message_stack.insert(0, path)
