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

# Define parameters for the experiments

wandb.config.epochs = 5
wandb.config.batch_size = 64
wandb.config.num_filters = 32
wandb.config.num_layers = 2
wandb.config.activation_fun = "relu"

# Data import
(x_train, y_train), (x_test, y_test) = get_data()

# Model creation
model = create_model(activation_fun = wandb.config.activation_fun, num_filters = wandb.config.num_filters, num_layers=wandb.config.num_layers)

# Model training
train_model(model, x_train, y_train, batch_size = wandb.config.batch_size, epochs=wandb.config.epochs)

# Save the entire model to a keras file
file_name = "saved_model.keras"
model.save(file_name)

# Log the model file 
artifact = wandb.Artifact("trained_model", type="model")
artifact.add_file(file_name)
wandb.log_artifact(artifact)

# Load the model from the file
loaded_model = keras.models.load_model(file_name)

# Save the ground truth and the predictions for further graphical analysis
ground_truth = np.argmax(y_test, axis=1)
predictions = predict_classes(loaded_model, x_test)

np.save("ground_truth.npy", ground_truth)
np.save("predictions.npy", predictions)

# Log predictions 
artifact = wandb.Artifact('predictions', type='predictions')
artifact.add_file('predictions.npy')
wandb.log_artifact(artifact)

# Model evaluation on test data
score = loaded_model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

# Log the test loss and accuracy

wandb.log({"test_loss": score[0], "test_accuracy": score[1]})

# Log all parameters in wandb
wandb.log({"epochs": wandb.config.epochs})
wandb.log({"batch_size": wandb.config.batch_size})
wandb.log({"num_filters": wandb.config.num_filters})
wandb.log({"num_layers": wandb.config.num_layers})
wandb.log({"activation_function": wandb.config.activation_fun})

wandb.finish()