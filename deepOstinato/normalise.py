class MinMaxNormaliser:
    """Applis MinMaxNormalisation to an array.
    Takes minimum and maximum values from transformed audio"""
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val

    def normalise(self, array):
        normalised_audio = (array - array.min()) / (array.max() - array.min())
        normalised_audio = normalised_audio * (self.max  - self.min) - self.min
        return normalised_audio

    def denormalise(self, normalised_audio, original_min, original_max):
        denormalised_audio = (normalised_audio - self.min) / (self.max - self.min)
        denormalised_audio = normalised_audio * (original_max - original_min) + original_min
        return denormalised_audio
