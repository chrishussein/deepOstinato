import librosa as lr
from sklearn.base import BaseEstimator, TransformerMixin
from deepOstinato.preprocessing.constants import PAD_SIZE

class Padder(BaseEstimator, TransformerMixin):
    """Pads audio, pad_size corresponds to total length of audio series."""
    def __init__(self, pad_size=PAD_SIZE):
        self.pad_size = pad_size

    def fit(self):
        """Fit method for the padder."""
        return self

    def transform(self, audio):
        """Transform method to pad the audio file."""
        return [lr.util.fix_length(piece, self.pad_size) for piece in audio]
