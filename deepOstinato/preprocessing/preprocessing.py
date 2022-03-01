from sklearn.base import BaseEstimator, TransformerMixin
from deepOstinato.preprocessing.filter_audio import filter_audio
from deepOstinato.preprocessing.short_time_fourier_transform import STFT
from deepOstinato.preprocessing.minmaxnormalizer import MinMaxNormaliser
from deepOstinato.preprocessing.pad import Padder
from deepOstinato.preprocessing.constants import FRAME_SIZE, HOP_SIZE
from sklearn.pipeline import Pipeline

#On .py to rull them all: gather all preprocessing steps to iterate over the files.

class Preprocessor(BaseEstimator, TransformerMixin):
    """All preprocessing steps from midi file to spectogram"""
    def __init__(self):
        pass

    def preprocess(self, path, max_size=55_000_000, min_size=20_000_000):

        audio = filter_audio(path, max_size=max_size, min_size=min_size)

        def set_pipeline(self, audio):
            """defines the pipeline with STFT, Normalization and Padding"""
            preprocessing_pipeline = Pipeline([
                ("STFT", STFT(audio, n_fft = FRAME_SIZE-1, hop_length = HOP_SIZE)),
                ("normalize", MinMaxNormaliser()),
                ("padding", Padder())
            ])
            return preprocessing_pipeline
