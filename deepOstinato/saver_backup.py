import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import os

<<<<<<< HEAD:deepOstinato/saver_backup.py
class npy_file_save:
    def __init__(self):
        pass

    def save(audio):
        counter = 1
        for npy in audio:
            np.save(f'raw_data/transformed_audio/npy_file_no{counter}', npy)
            counter += 1

class wav_file_save:
=======
class Saver(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def save(audio, path):
        """Method that save preprocessed audio file """
        for idx, npy in enumerate(audio):
            np.save(os.path.join(path, f"npy_file_no{idx}"), npy)
>>>>>>> 92737331e4cc44430056dbe5d8cfda9d286f6a52:deepOstinato/saver.py
