import tensorflow as tf
from tensorflow.keras import Sequential, layers
import keras
import numpy as np

X = 7
Y = 7
Z = 128
input_shape = [512]
x1 = 7
y1 = 7
z1 = 128


def generate_generator():
    generator = keras.models.Sequential([
        keras.layers.Dense(X*Y*Z, input_shape=input_shape),
        keras.layers.Reshape([X,Y,Z]),
        keras.layers.Conv2DTranspose(32, kernel_size = 3, strides =2, padding = 'same',activation = 'relu'),
        keras.layers.Conv2DTranspose(1, kernel_size = 3, strides =2, padding = 'same',activation = 'relu')
        ])
    return generator

def generate_discriminator():
    discriminator = keras.models.Sequential([
        keras.layers.Conv2D(64, kernel_size = 5, strides =2, padding = 'same' ,activation = 'relu'),
        keras.layers.MaxPooling2D(pool_size=(2,2)),
        keras.layers.Dropout(0.4),
        keras.layers.Dropout(0.4),
        keras.layers.Flatten(),
        keras.layers.Dense(1, activation = 'sigmoid')])
    return discriminator

def generate_gan(generator, discriminator):
    gan = keras.models.Sequential([generator, discriminator])
    return gan
