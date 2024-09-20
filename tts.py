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
                
                path, text = message_stack.pop()
                
                print()
                print(f"[now playing: {path}]")
                print(f"\"{text}\"")
                
                play_sound_file(path)
                count += 1

message_stack = []

sound_thread = threading.Thread(target=_play_stack)
sound_thread.start()


def text_to_file(args: tuple) -> str:
        count, text = args
        
        path = f"output{count}.mp3"
        
        try:
                file = gTTS(text=text)
                file.save(path)
        except AssertionError:
                print(f"ERROR WITH TTS FOR MESSAGE: [{text}]")
                quit()

        return path

def play_sound_file(path) -> None:
        mixer.init()
        mixer.music.load(path)
        mixer.music.play()
        
        while mixer.music.get_busy():
                time.sleep(.1)
        
        time.sleep(MESSAGE_DELAY)
        
        os.remove(path)

def add_to_stack(ind_text: str):
        path = text_to_file(ind_text)

        message_stack.insert(0, (path, ind_text[1]))
