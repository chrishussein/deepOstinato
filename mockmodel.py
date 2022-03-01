import tensorflow as tf
from tensorflow import Sequential, layers


def generator():
    x = 7
    y = 7
    z = 128
    x1 = 7
    y1 = 7
    z1 = 128

    model = Sequential()
    model.add(layers.Dense(x*y*z, input_shape=[7,7,128])),
    model(layers.Reshape([x1,y1,z1])),
    model(layers.conv2dtranspose(64, kernel_size = 5, strides =2, padding = 'same',activation = 'relu')),
    model.add(layers.Dense(10, activation = 'softmax'))

def discriminator():
    model = Sequential()
    model(layers.conv2dtranspose(64, kernel_size = 5, strides =2, padding = 'same' ,activation = 'relu')),
    model.add(layers.Dense(1, activation = 'softmax'))

model = Sequential()
gan = model(generator, discriminator)

discriminator.compile(loss='binary_crossentropy', optimizer = 'Adam')
discriminator.trainable = False
gan.compile(loss = 'binary_crossentropy', optimizer = 'Adam')

def train_gan(gan, dataset, batch_size, codings_size, n_epochs = 'XX'):
    generator, discriminator = gan.layers
    for epoch in range(n_epochs):
        for X_batch in dataset:
            noise = tf.random.normal(shape =[batch_size, codings_size])
            generated_images = generator(noise)
            X_fake_and_real = tf.concat([generated_images, X_batch], axis = 0)
            y1= tf.constant([[0.]]* batch_size + [[1.]] * batch_size)
            discriminator.trainable = True
            discriminator.train_on_batch(X_fake_and_real, y1)
            noise = tf.random.normal(shape = [batch_size,codings_size])
            y2 = tf.constant([[1.]] * batch_size)
            discriminator.trainable = False
            gan.train_on_batch(noise.y2)
