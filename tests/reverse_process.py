from deepOstinato.preprocessing.loader import Load_Numpy
from deepOstinato.preprocessing.normalise import MinMaxNormaliser, MinMaxDenormaliser
from deepOstinato.preprocessing.short_time_fourier_transform import ISTFT
from deepOstinato.preprocessing.saver import Saver

if __name__ == '__main__':

    sample_rate = 22050
    input_path = "raw_data/transformed_audio/"
    output_path = 'raw_data/postproc_wav_files/'

    loaded_audio = Load_Numpy.load(input_path)
    print(loaded_audio)
    scaler = MinMaxDenormaliser(0, 1)
    denormalised_audio = scaler.denormalise(loaded_audio, -65.5473, 14.452698)
    print(denormalised_audio)
    inversed_audio = ISTFT.istft(denormalised_audio)

    Saver.save_wav(output_path, inversed_audio, sample_rate)
