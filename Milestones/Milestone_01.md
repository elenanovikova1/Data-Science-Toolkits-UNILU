# Milestone 01

# Question 01 

- **About the Dataset**: The dataset consists of 70,000 images and labels (60,000 in 
the training set and 10,000 in the test set) of handwritten digits. 

- **Characteristics of the Dataset**: The images are 28x28 pixels, meaning 
they have a 28x28 grid of pixels, with each pixel having a grayscale 
value. The dataset's structure includes x\_train with a shape of (60000, 
28, 28). We identified it by using the following command in the code: 
```print("x_train shape:", x_train.shape)```. 
<br>
<br>
Each label is a digit (represented by an 8-bit unsigned integer, we got this by adding the following command in begginning of the code : ```print("label type: ", type(y_train[0])))```. Later, the data is transformed to a vector with 10 entries, where all entries except one are zero, and the position of the non-zero entry corresponds to the digit shown in the picture. For example, 
the label for the digit seven is (0;0;0;0;0;0;1;0;0;0).

- **Problem solved by the machine learning models**: Machine learning models solve the problem of determining digits represented on the images.

- **Classification or Regression Problem?**: This is a classification 
problem because it aims to predict the discrete and finite values (10 
different digits) represented by the images. Classification problems 
involve predicting a category, while regression problems estimate an 
unknown function based on function values.

# Question 02

Code was successfully obtained from github.

# Question 03

During the work on the project we learned also how to revert commit in order to have clean history in the repository. It can be done using the following commands in the terminal : 

- git revert “hash of the commit”
- git push

Hash of the commit can be found in the history of the commits on the github.

During our testing we have also spotted that the file was also deleted from the local machine, not only from the repository.

We also blocked all direct pushes to the main branch using Settings on the Github (Settings -> General -> Branches -> Branch protection rule -> Tick boxes "Require a pull request before merging" and "Require approvals" -> Save changes). 

We have created a new feature branch to work on and to push the changes to: feature/digits.

# Question 04
- **Step necessary to run the code**:
	- Download and install Python from www.python.org
	- Download and install some IDE for programming in Python (for example, PyCharm)
	- Create new PyCharm project
	- Create new *.py file in the PyCharm project
	- Go to Git using the link from the task (https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py)
	- Copy the code from the link (https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py)
	- Paste to the *.py file
	- Run
	- It can be the case that the program does not run. It can happen since the code imports some libraries that are not yet installed on the computer. Libraries can be installed using the following options:
		- Using PyCharm IDE: it highlights the missing libraries, do right click and proceed with intallation (Elena did this option and it worked out smoothly)
		- Using terminal: using a command "$ pip install" + "name of the library"
- **Versions are being used to run the code (python version and all
dependencies)**: General requirements and dependencies are listed in the README.md. During testing we had different experience due to different versions of the software on our machines.

	#### Florian:

		Systems where the code has been tested:
	 	* Linux ubuntu 22.4 
		* Python version: 3.10.12
		* Tensorflow version: 2.14.0
	 	* Keras version: 2.14.0
	 	* Numpy vesrion: 1.26.1

		* macOS Ventura 13.2.1
		* Python version: 3.11 
		* Tensorflow version: 2.14.0
	 	* Keras version: 2.12.0
	 	* Numpy vesrion: 1.23.5
	 	On macOS with M2 processor the code didn't run at first 
	 	- need to install tensorflow-macos first. 
	 	Which also resolved some dependency issues 
	 	-> takes older versions of numpy and keras 

	#### Elena:

		Systems where the code has been tested:
	 	* macOS Monterey 12.4
	 	* Python version: 3.8
	 	* Tensorflow version: 2.14.0
	 	* Keras version (the same as tensorflow): 2.14.0
	 	* Layers verion: 0.1.5
	 	* Numpy vesrion: 1.24.2
	 	Code worked smoothly after I installed the libraries. 
	 	Libraries intallation worked as expected.

- **Are the versions dependent on the system the code is being run on? (try running it on different machines, by checking out the code onto these machines. Does it work out of the box?)** 

For macOS Ventura 13.2.1 (M2) it didn't work out of the box. Needed to install tensorflow-macos first. 

# Question 05

- **What is the input to and the output from the neural network?**

Input: x\_train, y\_train; grayscale images of handwritten digits with dimension (28, 28, 1).

Output: The output of the model is a probability distribution over the classes (10 classes representing the different digits). Therefore the highest probability value determines the predicted class/cathegory for that input image.

```
model.summary()
```
Prints a summary of the model layers, the output shape and the parameters. 

- **What is Keras? And how does it relate to Tensorflow?**

Originally, Keras was an independent library in the Python with pre-designed functions for training nural networks. Since TensorFlow version 2.0, Keras is directly integrated into TensorFlow and us the API to use Tensorflow (computational backend for deep learning). The following model was applied in the code: Convolutional Neural Network with different layers (CNN).

- **How is the data loaded?**

The following command loads the data from the mnist module of keras and splits it into training and testing sets:

```
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
```
- **Which dependencies are imported?**

The following commands import the necessary packages, such as numpy (in the code it was used for operations with multi-dimentional arrays) and tensorflow (for machine learning / deep learning):

```
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
```
- **What kind of neural network architecture are you dealing with?**

CNN is a neural network architecture where the model is feature engineering itself and finding patterns in the images. The architecture of the CNN networks consists of multiple layers:

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

* Convolutional layer: Convolutional layers are used to detect patterns in the input data, like edges or textures. 
* Pooling Layer: Max-pooling is used to use the highest values of the feature map as input for the next layer. It Zooms out and summarizes information to keep important details.
* Flatten: It takes all the structured information and makes it flat, so it can be easily processed by certain types of neural network layers.
* Dropout: This adds a dropout layer with a dropout rate of 0.5. Dropout is a technique to prevent overfitting by randomly "dropping out" some neurons during training.
* Dense: Output layer. It takes all the information and combines it in various ways to make a final decision.

- **Other explanations on how the code works:**


```

"""
## Setup
"""


"""
## Prepare the data
"""

# Import of required libraries
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Model / data parametersh

# Number of labels used in the model (it identifies digits from 0 to 9, 
# that's why there are 10 classes)
num_classes = 10
# Format of the images used for the input
input_shape = (28, 28, 1)

# Load the data and split it between train and test sets
# x - images, y - labels
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
# Normalices values for the pictures to [0,1] for the grayscale value - 0 # representing white and 1 representing black

x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

# Reshapes the input data - the numpy function expand_dims adds on an additional
# dimension at the last position (-1) of the array. The dimension is for keras to 
# know the number of channels. In this case 1 for grayscales.  
# Prints the shape of the x__train and x__test data to the check the correct 
# dimension of the training data (28, 28, 1) and number of training and 
# test datasets (60,000 and 10,000). 


# convert class vectors to binary class matrices
# Pre-processing of label y. 
# Converts a class vector (integers) to binary class matrix 
# with the predefined number of classes: 10. (Required input format for Keras) 

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

"""
## Build the model
"""

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

"""
## Train the model
"""

# The model will train itself with the sample size of 128 per iteration and adapt the weights. The iteration will be conducted 15 times. 

batch_size = 128
epochs = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

"""
## Evaluate the trained model
"""
# Prints loss and accuracy of model tested on the test set. 
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

```


# Question 06

The documentation file README.md listing the dependencies has been added to the feature branch and will be merged into the main branch with a "Pull Request".

# Question 08

Folder "Milestones" created with the report milestone_01.md 

# Question 09

TBA

# Question 10

TBA




