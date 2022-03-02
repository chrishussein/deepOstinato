import librosa as lr
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from deepOstinato.preprocessing.constants import FRAME_SIZE, HOP_SIZE, SAMPLE_RATE

class STFT(BaseEstimator, TransformerMixin):
    """short-time Fourier transform"""
    def __init__(self):
        pass

    def stft(self, audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE, sample_rate=SAMPLE_RATE, transform="decibel"):
        """Returns the short-time Fourier transform version of an audio file,
        with additional transformation applied (according to selection)."""

        audio = np.array(audio)
        stft = lr.stft(audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE)
        #Convert to selected unit (decibel, mel or else)
        #mel_basis=lr.filters.mel(sample_rate, n_fft)
        #transform_type = {"decibel": lambda x: lr.power_to_db(x**2),                  #power spectrogram (amplitude squared) to decibel (dB) units
        #                              "mel": lambda x: lr.power_to_db(mel_basis.dot(x**2))}
        #return transform_type[transform](stft)

        return lr.power_to_db(audio**2)


class ISTFT:
    """inverse short_time Fourier transform"""

    def __init__(self):
        pass

    def istft(self, audio, transform="decibel"):

        #transform_type = {"decibel": lambda x: (lr.db_to_amplitude(x))**(1/2),
        #                              "mel": lambda x: x}       #TO IMPLEMENT!! sqrt(reverse power to db(reverse mel_basis dot stuff))
        #spectogram = transform_type[transform](audio)
        #inversed_audio = lr.istft(spectrogram)
        #return inversed_audio

        return lr.db_to_amplitude(audio)
