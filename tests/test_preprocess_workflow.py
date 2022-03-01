from cmath import log
from locale import normalize
from deepOstinato.filter_audio import filter_audio
from deepOstinato.midi_to_audio import midi_to_audio
from deepOstinato.constants import FRAME_SIZE, HOP_SIZE
from deepOstinato.short_time_fourier_transform import STFT

from deepOstinato.pad import Pad
from deepOstinato.normalise import MinMaxNormaliser
from deepOstinato.saver import Saver
from sklearn.preprocessing import MinMaxScaler



if __name__ == '__main__':
    input_audio_path = 'raw_data/sample_audio'


    padder = Pad(pad_size=1500000)

    audio = filter_audio(input_audio_path)

    padded_audio = padder.pad(audio)

    log_stft = STFT.stft(padded_audio, n_fft = FRAME_SIZE, hop_length = HOP_SIZE)
    scaler = MinMaxNormaliser(0, 1)

    normalised_audio = scaler.normalise(log_stft)
    saver = Saver
    saver.save(normalised_audio)
