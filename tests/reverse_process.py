from deepOstinato.preprocessing.loader import Load_Numpy
from deepOstinato.preprocessing.minmaxnormalizer import MinMaxNormaliser, MinMaxDenormaliser
from deepOstinato.preprocessing.short_time_fourier_transform import ISTFT
from deepOstinato.preprocessing.saver import Saver

if __name__ == '__main__':

    sample_rate = 22050
    input_path = "raw_data/transformed_audio/"
    output_path = 'raw_data/postproc_wav_files/'

    loaded_audio = Load_Numpy.load(input_path)
    scaler = MinMaxDenormaliser()
    scaler.fit()

    denormalised_audio = scaler.transform(loaded_audio)

    inversed_audio = ISTFT.istft(denormalised_audio)

    Saver.save_wav(inversed_audio, output_path, sample_rate)
