import numpy as np
import soundfile as sf
from sklearn.base import BaseEstimator, TransformerMixin
import os

class Saver(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def save_npy(audio, path):
        """Method that saves preprocessed audio files """
        for idx, npy in enumerate(audio):
            np.save(os.path.join(path, f"npy_file_no{idx}"), npy)

    def save_wav(audio, path, sample_rate):
        """Method that saves audio wav files """
        for idx, inversed_audio_piece in enumerate(audio):
            sf.write(f'{path}post_processed_audio_no{idx}.wav', inversed_audio_piece, sample_rate)
