from sklearn.base import BaseEstimator, TransformerMixin

class MinMaxNormaliser(BaseEstimator, TransformerMixin):
    """Applies MinMaxNormalisation to an array.
    Takes minimum and maximum values from transformed audio"""
    def __init__(self):
        pass

    def fit(self, array, switch):
        """Fit method for the normalizer.
        Takes in an array and a switch (boolean) which define if the normalizer should be fitted or not"""
        self.min_val = array.min()
        self.max_val = array.max()
        return self

    def transform(self, array, step):
        """Transform method that takes an array and normalize it (if step='pre'),
        or denormalize it (if step='post'). """
        if step == "pre":
            pass
        if step == "post":
            pass


    def normalise(self, array):
        normalised_audio = (array - array.min()) / (array.max() - array.min())
        normalised_audio = normalised_audio * (self.max  - self.min) + self.min
        return normalised_audio

class MinMaxDenormaliser(BaseEstimator, TransformerMixin):
    """Retransform the array to its original scale.
    Takes minimum and maximum values from transformed audio"""
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val

    def denormalise(self, normalised_audio, original_min, original_max):
        denormalised_audio = (normalised_audio - self.min) / (self.max - self.min)
        denormalised_audio = normalised_audio * (original_max - original_min) + original_min
        return denormalised_audio
