import librosa as lr
import matplotlib.pyplot as plt
from deepOstinato.constants import FRAME_SIZE, HOP_SIZE


def plot_spectrogram(Y, sr, hop_length=HOP_SIZE, y_axis='log'):
    plt.figure(figsize=(25, 10))
    lr.display.specshow(Y,
                        sr=sr,
                       hop_length = hop_length,
                       x_axis='time',
                       y_axis=y_axis)
    plt.colorbar(format="%+2.f")
