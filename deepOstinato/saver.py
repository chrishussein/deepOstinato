import numpy as np

class Saver:
    def __init__(self):
        pass

    def save(audio):
        counter = 1
        for npy in audio:
            np.save(f'raw_data/transformed_audio/npy_file_no{counter}', npy)
            counter += 1
