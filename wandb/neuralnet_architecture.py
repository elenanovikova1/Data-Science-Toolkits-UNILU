from tensorflow import keras
from keras import layers

def create_model(activation_fun = "relu", num_filters = 32, num_layers=2):

    num_classes = 10
    input_shape = (28, 28, 1)

    model = keras.Sequential()

    model.add(layers.Input(shape=input_shape))

    for _ in range(num_layers):
        model.add(layers.Conv2D(num_filters, kernel_size=(3, 3), activation=activation_fun))
        model.add(layers.MaxPooling2D(pool_size=(2, 2)))

    model.add(layers.Flatten())
    model.add(layers.Dropout(0.5))

    model.add(layers.Dense(num_classes, activation="softmax"))

    model.summary()

    return model