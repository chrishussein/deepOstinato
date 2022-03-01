from cmath import log
from locale import normalize
from deepOstinato.preprocessing.filter_audio import filter_audio
from deepOstinato.preprocessing.midi_to_audio import midi_to_audio
from deepOstinato.preprocessing.constants import FRAME_SIZE, HOP_SIZE
from deepOstinato.preprocessing.short_time_fourier_transform import STFT

from deepOstinato.preprocessing.pad import Pad
from deepOstinato.preprocessing.normalise import MinMaxNormaliser
from deepOstinato.preprocessing.saver import Saver
from sklearn.preprocessing import MinMaxScaler



if __name__ == '__main__':
    input_audio_path = 'raw_data/sample_audio'


    padder = Pad(pad_size=1500000)

    audio = filter_audio(input_audio_path)

    padded_audio = padder.pad(audio)

    log_stft = STFT.stft(padded_audio, n_fft = FRAME_SIZE, hop_length = HOP_SIZE)
    scaler = MinMaxNormaliser(0, 1)

    normalised_audio = scaler.transform(log_stft)
    saver = Saver
    saver.save(normalised_audio)
