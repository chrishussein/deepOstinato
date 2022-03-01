import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import os

class Saver(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def save(audio, path):
        """Method that save preprocessed audio file """
        for idx, npy in enumerate(audio):
            np.save(os.path.join(path, f"npy_file_no{idx}"), npy)
