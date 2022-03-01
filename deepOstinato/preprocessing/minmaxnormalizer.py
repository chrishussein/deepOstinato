from sklearn.base import BaseEstimator, TransformerMixin
from deepOstinato.preprocessing.constants import MAX_VAL, MIN_VAL

class MinMaxNormaliser(BaseEstimator, TransformerMixin):
    """Applies MinMaxNormalisation to an array.
    Takes minimum and maximum values from transformed audio"""
    def __init__(self):
        self.min_val = MIN_VAL
        self.max_val = MAX_VAL

    def fit(self):
        """Fit method for the normalizer"""
        return self

    def transform(self, array):
        """Transform method that takes an array and normalize """
        normalised_audio = (array - self.min_val) / (self.max_val - self.min_val)
        return normalised_audio


class MinMaxDenormaliser(BaseEstimator, TransformerMixin):
    """Retransform the array to its original scale."""

    def __init__(self):
        self.min_val = MIN_VAL
        self.max_val = MAX_VAL

    def fit(self):
        """Fit method for the denormalizer"""
        return self

    def transform(self, normalised_array):
        """Transform method that takes a normalized array and transforms it to its original scale """
        denormalised_array = normalised_array * (self.max_val - self.min_val) + self.min_val
        return denormalised_array
