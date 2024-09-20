from gtts import gTTS
from pygame import mixer

import threading
import os
import time


MESSAGE_DELAY: float = 1

def _play_stack():
        count = 0
        while True: 
                if not message_stack:
                        continue

                play_sound_file(message_stack.pop())
                count += 1

message_stack = []

sound_thread = threading.Thread(target=_play_stack)
sound_thread.start()


def text_to_file(args: tuple) -> str:
        count, text = args
        
        path = f"output{count}.mp3"
        file = gTTS(text=text)
        
        file.save(path)

        return path

def play_sound_file(path) -> None:
        print("now playing: " + path)
        
        mixer.init()
        mixer.music.load(path)
        mixer.music.play()
        
        while mixer.music.get_busy():
                time.sleep(.1)
        
        time.sleep(MESSAGE_DELAY)
        
        os.remove(path)

def add_to_stack(text: str):
        path = text_to_file(text)

        message_stack.insert(0, path)
