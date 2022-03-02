from cmath import log
from locale import normalize
from deepOstinato.preprocessing.filter_audio import filter_audio
from deepOstinato.preprocessing.midi_to_audio import midi_to_audio
from deepOstinato.preprocessing.constants import FRAME_SIZE, HOP_SIZE
from deepOstinato.preprocessing.short_time_fourier_transform import STFT

from deepOstinato.preprocessing.pad import Padder
from deepOstinato.preprocessing.minmaxnormalizer import MinMaxNormaliser
from deepOstinato.preprocessing.saver import Saver
from sklearn.preprocessing import MinMaxScaler



if __name__ == '__main__':
    input_audio_path = 'raw_data/sample_audio'
    output_path = 'raw_data/transformed_audio'


    padder = Padder()

    audio = filter_audio(input_audio_path)

    padded_audio = padder.transform(audio)

    log_stft = STFT.stft(padded_audio, n_fft = FRAME_SIZE, hop_length = HOP_SIZE)
    scaler = MinMaxNormaliser(0, 1)
    normalised_audio = scaler.transform(log_stft)
    saver = Saver()
    saver.save_npy(normalised_audio, output_path)
