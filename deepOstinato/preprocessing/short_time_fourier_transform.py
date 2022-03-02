import librosa as lr
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from deepOstinato.preprocessing.constants import FRAME_SIZE, HOP_SIZE

class STFT(BaseEstimator, TransformerMixin):
    """short-time Fourier transform"""

    def __init__(self):
        pass

    def stft(audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE, transform="decibel"):
        """Returns the log short-time Fourier transform version of an audio file"""

        audio = np.array(audio)
        stft = lr.stft(audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE)
        #Convert to selected unit (decibel, mel or else)
        mel_basis = 0 #DEFINE THIS!!!
        transform_type = {"decibel": lambda x: lr.power_to_db(x**2),                  #power spectrogram (amplitude squared) to decibel (dB) units
                                      "mel": lambda x: lr.power_to_db(mel_basis.dot(x**2))}
        return transform_type[transform](stft)


class ISTFT:
    """inverse short_time Fourier transform"""

    def __init__(self):
        pass

    def istft(audio):

        inversed_audio = lr.istft(audio)
        return inversed_audio
