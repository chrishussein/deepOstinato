from ast import Load
from cmath import log
import numpy as np
import os
from locale import normalize

from deepOstinato.preprocessing.filter_audio import filter_audio
from deepOstinato.preprocessing.midi_to_audio import midi_to_audio
from deepOstinato.preprocessing.constants import FRAME_SIZE, HOP_SIZE
from deepOstinato.preprocessing.short_time_fourier_transform import STFT, ISTFT, MelSpec, Inverse_Mel
from deepOstinato.preprocessing.pad import Padder
from deepOstinato.preprocessing.minmaxnormalizer import MinMaxNormaliser, MinMaxDenormaliser
from deepOstinato.preprocessing.saver import Saver
from deepOstinato.preprocessing.loader import Load_Numpy
from sklearn.preprocessing import MinMaxScaler

##############################################################################
######### AUDIO PROCESSING ------------------ deepOstinato ###################
##############################################################################

if __name__ == '__main__':
    # Paths
    input_audio_path = 'raw_data/sample_audio'
    npy_path = 'transformed_audio'
    output_audio_path = 'postproc_wav_files'
    transformed_audio_path = 'raw_data/pre_post_proc_mel'

    # Sample Rate
    sample_rate = 22050

    # Instanciations
    padder = Padder()
    saver = Saver()
    loader = Load_Numpy()
    short_fft = STFT()
    inv_short_fft = ISTFT()
    mel_gram = MelSpec()
    inv_mel_gram = Inverse_Mel()

    # Load, Filter, Pad, STFT the Audio
    audio = filter_audio(input_audio_path)
    padded_audio = padder.transform(audio)
    #log_stft = short_fft.stft(padded_audio, n_fft = FRAME_SIZE, hop_length = HOP_SIZE)
    mel_spec_audio = mel_gram.mel_spec(padded_audio)

    # Set Max Value and Optimization Increment
    n = 5
    increment = 0.5

    # Iterate Max Value
    for i in range(0, 10):

        # Preprocess and Post-Process Audio while iterating thrugh max values

        #Create directory to store Max Value output
        max_val_directory_num = round(n, 2)
        max_val_directory = f'Max_val_equal_to_{round(n, 2)}'
        max_val_output_path = os.path.join(transformed_audio_path, max_val_directory)
        os.makedirs(max_val_output_path)

        # Set Min Value
        m = -5
        # Iterate Min Value (Preprocess and save npy)
        for q in range(0, 10):

            #Create directory to store Min Value output
            min_val_directory_num = round(m, 2)
            min_val_directory = f'Min_val_equal_to_{round(m, 2)}'
            min_val_npy_output_path = os.path.join(max_val_output_path, npy_path, min_val_directory)
            os.makedirs(min_val_npy_output_path)

            # Process Audio and save npy files while changing min values
            scaler = MinMaxNormaliser(min_val=m, max_val=n)
            m += increment #Increase Min Val
            normalised_audio = scaler.transform(mel_spec_audio)
            saver = Saver()
            print(normalised_audio)
            saver.save_npy(normalised_audio, f'{min_val_npy_output_path}/')

        # Reset Min Value
        m = -5

        # Iterate Min Value (Postprocess and save wav)
        for q in range(0, 10):

            #Create directory to store Audio output
            min_val_directory_num = round(m, 2)
            proc_audio_directory = f'Audio_{round(m, 2)}'
            min_val_audio_output_path = os.path.join(max_val_output_path, output_audio_path, proc_audio_directory)
            os.makedirs(min_val_audio_output_path)

            #Load processed audio and save post processed wav files
            loaded_audio = loader.load_npy_audio(f'{min_val_npy_output_path}/')
            m += increment #Increase Min Val
            scaler = MinMaxDenormaliser(min_val=m, max_val=n)
            loaded_audio = np.array(loaded_audio)
            denormalised_audio = scaler.transform(loaded_audio)
            #inversed_audio = inv_short_fft.istft(denormalised_audio)
            inversed_audio = inv_mel_gram.imel(denormalised_audio)
            saver.save_wav(inversed_audio, f'{min_val_audio_output_path}/', sample_rate)

        #Increase Max Value
        n -= increment
