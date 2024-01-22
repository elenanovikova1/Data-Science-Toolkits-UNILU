#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:03:38 2023

@author: floriangoldinger

Title: Simple MNIST convnet
Author: [fchollet](https://twitter.com/fchollet)
Date created: 2015/06/19
Last modified: 2020/04/21
Description: A simple convnet that achieves ~99% test accuracy on MNIST.
Accelerator: GPU

## Setup
"""

import numpy as np
from tensorflow import keras
import wandb
from wandb.keras import WandbCallback

from load_and_prepare_data import get_data
from neuralnet_architecture import create_model
from neuralnet_training import train_model
from prediction import predict_classes

# Initialize W&B
wandb.init(project="cnn_digits", config={"metric_to_optimize": "accuracy"})

# Data import
(x_train, y_train), (x_test, y_test) = get_data()

# Model creation
model = create_model()

# Model training
train_model(model, x_train, y_train)

# Save the entire model to a keras file
file_name = "saved_model.keras"
model.save(file_name)

# Log the model file 
artifact = wandb.Artifact("trained_model", type="model")
artifact.add_file(file_name)
wandb.log_artifact(artifact)

# Load the model from the file
loaded_model = keras.models.load_model(file_name)

# Prediction of the digit on the first 10 elements of test data
predicted_class = predict_classes(loaded_model, x_test[0:10])
print("Predicted Classes:", predicted_class)
print("True Classes:", np.argmax(y_test[0:10], axis=1))

# Model evaluation on test data
score = loaded_model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

# Log the test loss and accuracy
wandb.log({"test_loss": score[0], "test_accuracy": score[1]})