import librosa as lr
import numpy as np
from deepOstinato.constants import FRAME_SIZE, HOP_SIZE

class STFT:
    """short-time Fourier transform"""

    def __init__(self):
        pass

    def stft(audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE):
        """Returns the log short-time Fourier transform version of an audio file"""
        stft = lr.stft(audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE)
        stft = np.abs(stft) ** 2
        log_stft = lr.power_to_db(stft)
        return log_stft
