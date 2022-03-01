import numpy as np


class Load_Numpy:
    def __init__(self):
        pass

    def load():
        counter = 1
        loaded_audio = []
        for npy in npy_files:
            loaded =  np.load(f'raw_data/transformed_audio/npy_file_no{counter}', npy)
            loaded_audio.append(loaded)
            counter += 1
        return loaded_audio
