import librosa as lr

class Pad:
    """Pads audio, pad_size corresponds to total length of audio series"""
    def __init__(self, pad_size=1500000):
        self.pad_size = pad_size


    def pad(self, audio):
        padded_audio_pieces = []
        for piece in audio:
            padded_audio_piece = lr.util.fix_length(piece, self.pad_size)

            padded_audio_pieces.append(padded_audio_piece)
        return padded_audio_pieces
