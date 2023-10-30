## Milestone 01

### Question 01 

**1) Problem and Dataset Description**

- **About the Dataset**: The dataset consists of 70,000 images (60,000 in 
the training set and 10,000 in the test set) of handwritten digits, each 
labeled to indicate the digit it represents. Each label is a vector with 
10 entries, where all entries except one are zero, and the position of the 
non-zero entry corresponds to the digit shown in the picture. For example, 
the label for the digit seven is (0;0;0;0;0;0;1;0;0;0).

- **Classification or Regression Problem?**: This is a classification 
problem because it aims to predict the discrete and finite values (10 
different digits) represented by the images. Classification problems 
involve predicting a category, while regression problems estimate an 
unknown function based on function values.

- **Characteristics of the Dataset**: The images are 28x28 pixels, meaning 
they have a 28x28 grid of pixels, with each pixel having a grayscale 
value. The dataset's structure includes x_train with a shape of (60000, 
28, 28, 1).

### Question 4 

- **Pyhton versions and dependencies**: Are listed in the README.md
Systems where the code has been tested:
- macOS
- Linux ubuntu

On macOS the code didn't run at first - need to install tensorflow-macos first. 

Solution: docker for the different systems? 

### Question 5

**Explain the code*

**Dependencies**
```
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
```

Imports the necessary packages numpy (for numerical operations) and tensorflow (for machine learning / deep learning)

**Parameters**
```
num_classes = 10
input_shape = (28, 28, 1)
```

Specifies the parameters of the model.
num_classes: number of classes in the classification problem. E.g. 10 for the different digits 
input_shape: specifies the shape of the input data - in this case image with dimension 28 x 28 pixels with 1 channel (grayscales only)

**Loading data**
```
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
```

Loads the data from the mint module of keras and splits it into training and testing sets 

**Pre-processing**
```
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
```
Normalices values for the pictures to [0,1] for the grayscale value - 0 representing white and 1 representing black 

```
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")
```
Reshapes the input data - the numpy function expand_dims adds on an additional dimension at the last position (-1) of the array. The dimension is for keras to know the number of channels. In this case 1 for grayscales. 
Prints the shape of the x_train and x_test data to the correct dimension of the training data (28, 28, 1) and number of train and test datasets (60,000 and 10,000). 

```
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
```
Pre-processing of prediction data y. Converts a class vector (integers) to binary class matrix with the predefined number of classes: 10. 


**Build model**
```
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()
```
Model applied: Convolutional Neural Network with different layers (CNN).
Method where the model is feature engineering itself and finding patterns in the images. 

Layers applied:
- Convolutional layer: Convolutional layers are used to detect patterns and features in images.
- Pooling Layer: Max-pooling is used to reduce the dimensions of the feature maps obtained from the convolutional layers.
- Flatten: 
- Dropout: This adds a dropout layer with a dropout rate of 0.5. Dropout is a regularization technique used to prevent overfitting by randomly "dropping out" some neurons during training.
- Dense: output layer 

Input: Grayscale images of handwritten digits with demension (28, 28, 1) 
Output: The output of the model is a probability distribution over the classes (10 classes representing the different digits) 

```
model.summary()
```
Prints a summary of the model layers, the output shape and the parameters. 

**Model training**

```
batch_size = 128
epochs = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
```
The model will train itself with the sample size of 128 per iteration and adapt the weights. The iteration will be conducted 15 times. 

**Evaluate**
```
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
```
Prints loss and accuracy of model. 








