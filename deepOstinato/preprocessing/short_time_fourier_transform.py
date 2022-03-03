import librosa as lr
from librosa.feature import melspectrogram
from librosa.feature.inverse import mel_to_audio

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

        return lr.power_to_db(np.abs(stft)**2)


class ISTFT:
    """inverse short_time Fourier transform"""

    def __init__(self):
        pass

    def istft(self, audio, transform="decibel"):

        #transform_type = {"decibel": lambda x: (lr.db_to_amplitude(x))**(1/2),
        #                              "mel": lambda x: x}       #TO IMPLEMENT!! sqrt(reverse power to db(reverse mel_basis dot stuff))
        #spectogram = transform_type[transform](audio)
        # spectrogram = lr.db_to_power(audio)
        # spectrogram = np.abs(spectrogram)**(1/2)
        inversed_audio = lr.istft(audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE)
        return inversed_audio

        #return lr.istft(lr.db_to_amplitude(audio))

class MelSpec(BaseEstimator, TransformerMixin):
    """short-time Fourier transform"""
    def __init__(self):
        pass

    def mel_spec(self, audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE, sample_rate=SAMPLE_RATE, transform="decibel"):
        """Returns the short-time Fourier transform version of an audio file,
        with additional transformation applied (according to selection)."""

        audio = np.array(audio)
        mel_spec_audio = lr.feature.melspectrogram(y=audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE, sr=SAMPLE_RATE)
        #Convert to selected unit (decibel, mel or else)
        #mel_basis=lr.filters.mel(sample_rate, n_fft)
        #transform_type = {"decibel": lambda x: lr.power_to_db(x**2),                  #power spectrogram (amplitude squared) to decibel (dB) units
        #                              "mel": lambda x: lr.power_to_db(mel_basis.dot(x**2))}
        #return transform_type[transform](stft)

        return mel_spec_audio

class Inverse_Mel:
    """inverse short_time Fourier transform"""

    def __init__(self):
        pass

    def imel(self, audio, sample_rate=SAMPLE_RATE, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE) :

        #transform_type = {"decibel": lambda x: (lr.db_to_amplitude(x))**(1/2),
        #                              "mel": lambda x: x}       #TO IMPLEMENT!! sqrt(reverse power to db(reverse mel_basis dot stuff))
        #spectogram = transform_type[transform](audio)
        # spectrogram = lr.db_to_power(audio)
        # spectrogram = np.abs(spectrogram)**(1/2)
        inversed_audio = lr.feature.inverse.mel_to_audio(audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE, sr=SAMPLE_RATE)
        return inversed_audio

        #return lr.istft(lr.db_to_amplitude(audio))
