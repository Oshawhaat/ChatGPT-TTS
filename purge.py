import os

for file in os.listdir("./"):
    if file.endswith(".mp3"):
        os.remove(file)