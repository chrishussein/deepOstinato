import os
import librosa as lr
import numpy as np

class Load_Numpy:
    def __init__(self):
        pass

    def load_npy_audio(self, path):
        loaded_audio = []
        for filename in os.listdir(path):
            loaded, rate = lr.load(os.path.join(path, filename))
            loaded_audio.append(loaded)
        return loaded_audio

    def load_npy_minmax(self, path):
        loaded_minmax = []
        for filename in os.listdir(path):
            loaded = np.load(os.path.join(path, filename), allow_pickle=True)
            loaded_minmax.append(loaded)
            return loaded_minmax
