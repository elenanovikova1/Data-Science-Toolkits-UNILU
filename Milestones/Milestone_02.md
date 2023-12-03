# Milestone 02

## Task 1

We have already added gitignore file to our repository. We continuously update this file when needed.

### Why you added a certain "ignore" to the file

The main idea is to avoid unnecessary files in the repository. Currently, there are the following files to be avoided: 

- All technical files with the following dimentions: .DS_Store .idea/
- Model that created by neural network in the code with the following filename: saved_model.h5, saved_model.keras

### Control over gitignore file

We version-control the ".gitignore" file. In our case, the most efficient strategy is to work in the same branch together because we can update each other quickly. We also before created separately our own branches for pure testing (to understand how git works before working on the project).

Since we worked in the same branch we did not have any issues with the update of the ".gitignore" file. As we understood, there was not strict requirement to work in separate branches and we chose the most efficient way for our team to do the project.

## Task 2

### What is a Hash Function?

A hash function is a mathematical algorithm that, given an input, produces a fixed-size string. These functions are primarily used for security purposes, such as integrity validation and digital signatures. One example of a hash function is SHA-256 (Secure Hash Algorithm 256-bit, to be used in the milestone), which generates an alphanumeric string of 256 bits.

#### Example:

**Input:** "This is an example"  
**Output:** `a1595c7ce2ce119b98bf3b3d9cd4dba9c7d03791af727c76c0e020fc3ea94cfc`

#### Main Characteristics of Hash Functions:

1. **Fixed Size:** The output is of a fixed size. For instance, SHA-256 always produces a 256-bit output, regardless of the input length. But the input should not be longer than 256 bit. 

2. **Deterministic:** The same input always generates the same output hash value.

3. **Irreversibility:** It is computationally infeasible to reverse an output hash value back to the input. Hash functions work only in the direction of input to output.

4. **Collision-Free:** Different inputs result in different outputs. Although collisions (two different inputs producing the same output) are theoretically possible, the probability is extremely low.

5. **Avalanche Effect:** Even a minor change in the input leads to a significant and unpredictable change in the output.

### What is a Python Module, Package, and Script? How Do They Differ from One Another?

#### Script:

A script is a standalone Python file (`.py`) that is directly executable. It consists of Python statements and instructions for performing specific tasks or operations.

**Key Features:**
- Executable file with a sequence of Python code.
- Runs directly using the Python interpreter.

#### Module:

A module is a `.py` file meant to be imported by other scripts or modules. It contains functions, classes, and variables that can be utilized by the importing script or module.

**Key Features:**
- Meant to be reused by importing it into other scripts or modules.
- Organizes code within a single file.
- Enhances code modularity and reusability.

#### Package:

Packages are sets of related modules. These modules work together and are stored in a common folder. A package typically includes an `__init__.py` file, signaling to Python that it is a package and specifying where the modules are stored.

**Key Features:**
- Organizes multiple related modules in a directory. 
- Improves organization of different modules. 

**Hierarchy of Script-Module-Package:**

- A script is a standalone executable file.
- Modules are individual files containing functions, classes and variables to be imported by scripts or other modules. 
- Packages are directories containing related modules, forming a structured and modular organization for related tasks.

### How would you explain a Docker container and volume to a child? 

Docker Container and Volumes: 

Consider this scenario: you and your friend both want to run software on your respective laptops, but there's a challenge – you have a Windows laptop, and your friend has an Apple laptop, with significantly different settings. This is where Docker containers and volumes can help. 

When creating new software, it might work perfectly well on your laptop but not on that of your friend. 

Docker containers are like closed boxes. They not only hold the software itself but also all the necessary information and settings for the software to run on different laptops (e.g. Apple and Windows). Because all the information needed is in the container, the software can run without problem in the container on different computers. 

Now, sometimes the software needs access to data stored on your computer. Then you need volumes. One can imagine volumes like holes in the container, allowing the software to access data that is stored outside of the container. Without volumes (holes), containers could not access any data that is stored outside of this box (container). 

### What is your preference concerning the use of Python virtualenv and Docker? When would you use one
or the other?

For professional software projects, Docker is preferable to virtual environments because it automates the installation of dependencies and ensures the correct Python version. In contrast, with virtual environments, these steps must be repeated each time the software is run on a new computer where the same virtual environment is not yet set up. Virtual environments are also less resilient to mistakes, requiring careful checking and manual installation of dependencies.

With Docker, dependencies are precisely defined and automatically installed with the container image, streamlining the setup process.

Especially in a collaborative environment, where different developers are involved, the correct dependencies management and the consistency of the environment can be ensured by Docker. 

Virtual environments (venvs) could be preferred in quick trials or lightweight projects that don't necessitate running on different systems or adapting dependencies in the future. 

### What is the Docker build context?

The Docker build context is the folder that contains all the necessary files required to build a Docker image. This typically includes essential files such as:

.py (script)
requirements.txt (dependencies)
Data.csv (data that the script utilizes)

When you initiate the Docker build process, Docker uses the contents of this specified folder as the foundation for creating the Docker image. 
The files within the build context are referenced in your Dockerfile, telling Docker on what to include in the image. The build context includes all the relevant components needed to successfully construct the Docker image. The COPY command in your Dockerfile is then used to copy files from the build context into the image.

### How can you assess the quality of a python package on PyPI?

PyPI is an open platform, anyone can publish packages on PyPI and there is no central quality assessment. Therefore a package could also be malicious or contain a virus. 

Therefore it makes sense to take a little bit of research to ensure quality and trustability of the package and its developers. Quality checks could include:

- Check if the package has a clear and consistent documentation 
- Version history of package
- Community ratings, comments on stack overflow
- Community involvement on the respective Git Hub repository 

But also simple indicators like stars and forks on PyPI can be an indicator. If there is very low community involvement, the package might not be secure. 

# Task 3

### Can code load the data? ###

Yes, code successfully loads the data. Data upload is performed using the following command in the code:

```(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()```

### Can code train (fit) a neural network on the data? ###

Yes, it can. Code trains a neural network on the data using the following command in the code:

```
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
```

### Can code save a fitted model to a ".h5" file (or saved model type for newer Tensorflow 2.0 versions)? ###

No, initial version of the code does not save a fitted model to a ".h5" file. We need to modify the code by adding few commdand for Tensorflow 2.14.0 version. Initially we added the following lines:

```
file_name = "saved_model.h5"
model.save(file_name)
```

We got warning that the format should be different:

```
UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
```

The code was amended accordingly:

```
file_name = "saved_model.keras"
model.save(file_name)
```

and it worked as expected without errors. File was saved to the folder with the code. We also amended gitignore file accordingly in order to exclude it from push.

### Can code load a ".h5" file, using Keras (or saved model type for newer Tensorflow 2.0 versions)? ###

No, initial version of the code does not load a fitted model from a ".h5" file. We need to modify the code by adding the follwoing command:

```
loaded_model = keras.models.load_model(file_name)
```
recall that ```file_name = "saved_model.keras"```.

### Can code perform predictions using a "fitted" model, using Keras? ###

No, initial version of the code does not perform predictions using the model. We need to modify the code by adding the follwoing command:

```
prediction = loaded_model.predict(x_test[0:1])
predicted_class = np.argmax(prediction, axis=1)
print("Predicted Class:", predicted_class)
print("True Class:", y_test[0:1])
```
We remark that the original code contains evaluation of the model of all test samples and outputs test loss and test accuracy.

# Task 4

### Split your code base into modules ###
We splitted the code into several modules:

```from load_and_prepare_data import get_data``` : this module containes the function get_data that loads the data and splits it between train and test sets, and then converts it for further usage

```from neuralnet_architecture import create_model``` : this module contains the function create_model that creates the nural network

```from neuralnet_training import train_model```  : this module contains the function train_model that trains the nural network

```from prediction import predict_classes``` : this module contains the function predict_classes that predicts digits from images

Native naming makes it easier to navigate within the code.

### The reasoning behind modularization and why we chose to structure the code like this

There were the following main reasons why we did it such way:

1. Modules are logically different from each other
2. Each module might be used separately later
3. I also makes sense to create modules such way that we can easily separate (make as comment) parts that require significant time to execute (for example, now we can make as comment part where code creates the model and we can easily use already saved model for testing that does not require model creation)
3. There was no sense to segregare one line of code into separate module (even though it performed a particular task), for example ```model.save(file_name)```

We used Python functions in order to import from our modules. 

###  Main file

We created one "main.py" script that calls the code/functions in all the other modules.

###  Imports in modules

Our modules contains imports that are required to perform funcitons within modules. For example, neuralnet_architecture module requires to import the following packages:

```
from keras import layers
```
```
from tensorflow import keras
```
###  PEP8 conformity

Our code is consistent with PEP8.


## Task 5

We created a requirements file `requirements.txt` with the following content and according to the dependencies identified in the first Milestone_01:

```
tensorflow==2.14.0
numpy==1.23.5
```

To create a new virtual environment and to activate it you need to proceed with this steps:

```
$ python3 -m venv venv #creates the virtual environment named venv
$ source venv/bin/activate #activates the virtual environment where you can install the required packages
```

In the activated virtual environment the following steps are necessary to run the installations specified in the requirements file: 

```
(venv) $ pip install -r requirements.txt
```

To test if all the required packages are installed you can execute which shows the packages installed within this virtual environment:

```
(venv) $ pip list
```
<<<<<<< Updated upstream

## Task 6

We created a ```Dockerfile``` that uses the tensorflow base-image from Docker Hub: 

```
# Image of tensorflow developers 
FROM tensorflow/tensorflow:2.14.0

WORKDIR /app

# loads the below files into the directory /app of the Docker container 
COPY requirements.txt .
COPY main.py .
COPY load_and_prepare_data.py .
COPY neuralnet_architecture.py .
COPY neuralnet_training.py . 
COPY prediction.py .

# Installs the packages 
RUN pip install -r requirements.txt

# Executes main.py with the Interpreter 
CMD python main.py
```

To build a Docker container based on the image  you have to execute the following command in the directory of the Dockerfile:

```
$ docker build -t digits:1.0 .
```

To run the main.py script in the container use this command:

```
$ docker run digits:1.0 
```
To have access to data stored on the local directory outside of the container, a volume has to be activated with this command:

```
docker run -v $(pwd):/app/ -it digits:1.0
```

This links the local directory pwd to the /app/ directory in the container and allows the app to access data outside of the container (e.g. the stored trained model).   

We have also both tested it and it worked on different computers with Intel processor but not on the MacBook Pro with ARM processor. Apparently the base image from tensorflow is not compatible with this processor architecture. 

```
floriangoldinger@Florians-MacBook-Pro project_01 % docker run digits:1.0
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
```

Also when run on the virtual machine on Ubuntu an error message appears on this same laptop. 

```
> [9/9] RUN pip install -r requirements.txt:
0.178 exec /bin/sh: exec format error
------
Dockerfile:14
--------------------
  12 |     
  13 |     
  14 | >>> RUN pip install -r requirements.txt
  15 |     
  16 |     CMD python main.py
--------------------
ERROR: failed to solve: process "/bin/sh -c pip install -r requirements.txt" did not complete successfully: exit code: 1
```

As to our research, this could also be related to the processor architecture (exec format error) and that we could not use this base image on a ARM processor. Unfortunately we lack the knowledge to address this issue on how to build a container on images that support different processor architectures. Additionally we would have to add other dependencies, because we saw in Milestone_01 that the script only works on the ARM processor when tensorflow-macos was installed. 

In order to control Docker build context we created a ".dockerignore" file.
