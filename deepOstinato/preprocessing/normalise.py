from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class MinMaxNormaliser(BaseEstimator, TransformerMixin):
    """MinMax Normalization transforms the minimum values of the features in 0s and the maximum values into 1s"""
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val

    def normalise(self, array):
        normalised_audio = (array - array.min()) / (array.max() - array.min())
        normalised_audio = normalised_audio * (self.max  - self.min) - self.min
        return normalised_audio

class MinMaxDenormaliser(BaseEstimator, TransformerMixin):
    """Retransform the array to its original scale.
    Takes minimum and maximum values from transformed audio"""
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val

    def denormalise(self, audio, original_min, original_max):
        audio = np.array(audio)
        denormalised_audio = (audio - self.min) / (self.max - self.min)
        denormalised_audio = audio * (original_max - original_min) + original_min
        return denormalised_audio
