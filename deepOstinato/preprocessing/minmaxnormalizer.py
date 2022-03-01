from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from deepOstinato.preprocessing.constants import MAX_VAL, MIN_VAL

class MinMaxNormaliser(BaseEstimator, TransformerMixin):
    """Applies MinMaxNormalisation to an array.
    Takes minimum and maximum values from transformed audio"""
    def __init__(self, min_val = MIN_VAL, max_val = MAX_VAL):
        self.min_val = min_val
        self.max_val = max_val

    def fit(self):
        """Fit method for the normalizer"""
        return self

    def transform(self, array):
        """Transform method that takes an array and normalize """
        normalised_audio = (array - self.min_val) / (self.max_val - self.min_val)
        return normalised_audio


class MinMaxDenormaliser(BaseEstimator, TransformerMixin):
    """Retransform the array to its original scale."""

    def __init__(self, min_val = -65.5473, max_val = 8.452698):
        self.min_val = min_val
        self.max_val = max_val


    def fit(self):
        """Fit method for the denormalizer"""
        return self

    def transform(self, normalised_array):
        """Transform method that takes a normalized array and transforms it to its original scale """
        normalised_array = np.array(normalised_array)
        denormalised_array = normalised_array * (self.max_val - self.min_val) + self.max_val
        return denormalised_array
