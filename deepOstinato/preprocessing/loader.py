import numpy as np
import os

class Load_Numpy:
    def __init__(self):
        pass

    def load(path):
        loaded_audio = []
        for filename in os.listdir(path):
            print(filename)
            loaded = np.load(f"{path}/{filename}")
            print(loaded)
        return loaded_audio
