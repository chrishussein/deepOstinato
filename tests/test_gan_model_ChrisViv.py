import tensorflow as tf
from tensorflow.keras import Sequential, layers
import numpy as np
import os
import wave
import librosa as lr

from keras.layers import Input, Dense, Reshape, Flatten, Dropout
from keras.layers.convolutional import Conv2D
from keras.models import Sequential, Model

from deepOstinato.preprocessing.constants import *
from deepOstinato.models.model_trial_Viv import GAN, discriminator_loss, cross_entropy, train_gan

if __name__ == '__main__':

    input = 0
    X_train = np.array(input)
    X_train = np.expand_dims(X_train, axis=3)

    gan_generator = GAN()
    generator = gan_generator.build_generator()
    discriminator = gan_generator.build_discriminator()

    discriminator.compile(optimizer="Adam", loss=discriminator_loss)

    gan = Sequential([generator, discriminator])
    gan.compile(optimizer="Adam", loss=cross_entropy)

    train_gan(gan=gan, dataset=X_train, batch_size=32, n_epochs = 50)
