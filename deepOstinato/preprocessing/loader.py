import numpy as np
import os

class Load_Numpy:
    def __init__(self):
        pass

    def load(path):
        loaded_audio = []
        for filename in os.listdir(path):
            loaded = np.load(f"{path}/{filename}", allow_pickle=True)
            loaded_audio.append(loaded)
        return loaded_audio
