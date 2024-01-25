# Milestone 04

## Task 1

### What is Experiment Management and why is it important?

Experiment Managements refers to the systematic organisation and tracking of experiments during the development and training of predictive models (in our case a convolutional network). The model is based on a multitude of parameters (e.g. data used, preprocessing steps, model architecture, hyperparameters). Experiments should identify the causal effect of the change of one parameter (keeping the other ones fix) on the outcome/prediction. 

Given the diversity of parameters involved in these experiments, it can be challenging to keep track of all the variations. Especially in a collaborative software project involving multiple team members, a systematic approach to documenting experiments becomes crucial. This systematic approach ensures that the organization can maintain knowledge about the experiments conducted, allowing team members to understand and build upon each other's work.

### What is a Metric in ML?

A metric in machine learning is a quantitative measure used to assess the performance of a model. It provides a summarized numerical evaluation of how well the model performs on a specific task, given a set of parameters.

### What is Precision and Recall? Why is there often a Trade-off between them?

*Precision* is the ratio of true positives to the sum of true positives and false positives. In the example of spam, it measures how many of the emails detected as spam are actually spam. 
*Recall* is the ratio of true positives to the sum of true positives and false negatives. For spam, it measures on how much of the actual spam I found. Did I detect all of them. 

There is a trade-off between precision and recall because improving one can lead to a deterioration of the other metric. It depends on the context on what is more important.

For example cancer diagnosis, where the goal is to detect all patients actually suffering from cancer, recall becomes crucial. It's more acceptable to have a few false positives (patients without cancer being incorrectly identified) if it means capturing all or most of the true positive cases (patients with cancer).

On the other hand, in the context of spam detection, where the goal is to avoid marking legitimate emails as spam, precision becomes more critical. Accepting a few false negatives (spam emails not detected) may be more tolerable if it means minimizing the number of false positives (legitimate emails incorrectly marked as spam).

### What is AUROC Metric?

AUROC is the abbreviation for Area Under the Receiver Operating Characteristic curve. 

The Receiver Operating Characteristic curve plots the true Positive rate against the False positive rate in a classification model. It plots the trade-off between TP and FP. 
The AUROC therefore measures the are under this curve for different thresholds. A higher AUROC value indicates better performance.

### What is a Confusion Matrix?

A confusion matrix is a table used in the evaluation of a classification model's performance. It provides an overview of how well a model is performing by comparing the predicted classes to the actual classes. The four main components of a confusion matrix are:

True Positives (TP):
These are the cases where the model correctly identified the positive class.

False Positives (FP):
These are the cases where the model predicted the positive class, but the true class was actually negative.

True Negatives (TN):
These are the cases where the model correctly identified the negative class.

False Negatives (FN):
These are the cases where the model predicted the negative class, but the true class was actually positive.

## Task 2

In order to execute this task we generated different files in the new folder ```wandb``` containing the following adapted or new files to execute experiments and save them to W&B:

- Adapted python scripts including wandb (```main_wandb.py```)
- ```Dockerfile``` (including ENTRYPOINT)
- ```.env``` (where the environment variable $WANDB_TOKEN is stored) -> included .env in .gitignore to not share the token publicly 
- ```entrypoint.sh```
- ```requirements.txt``` 

### Dockerfile

Added the shell script entrypoint.sh to access wandb: 
```COPY entrypoint.sh . ``` 

Set the entrypoint script as executable and run it to access the API of wandb:

```
RUN chmod +x .entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]
```

Even that the entrypoint.sh in the container was set executable we got an error message concerning permission rights. We first also had to set the permission rights for the local file before creating the container. Done with the following command: 

```chmod +x entrypoint.sh```

Then it worked. 

### .env

This file contains the environment_variable for the w&b token that the entrypoint is accessing through a volume on the local machine: 

```
WANDB_TOKEN=XXX
```

### entrypoint.sh

Created the file as explained in the Milestone_04 task sheet. It didn't run at first. Had to specify where the script can find the access token. We added the following line as the token is saved in the file .env:

```
source .env
```

### requirements.txt

The latest version of w&b was added: ```wandb==0.16.2```

### Build and run the container

To build the container the same command as in Milestone_02 was applied: 

```
$ docker build -t digits_wandb:1.0 .
```

The container was run using a volume that the shell script can access the W&B token in .env:

```
docker run -v $(pwd):/app/ -it digits_wandb:1.0
```

The script ```main_wandb.py```run. The following code was added to execute experiments and save the results in the cloud: 

### Script main_wandb.py 

Adapted code to log the experiments. Which means that the different functions had to be parameterized such that the parameters can be changed in the main_wandb.py file during training. No new image necessary as we build up a volume, so we can directly change the parameters. The scripts are available in the folder ```wandb```. 

The metrics and parameters then are logged into W&B to track the different experiments, the W&B projects are public under: 

[https://wandb.ai/dsta_unilu/cnn_digits?workspace=user-florian-goldinger](https://wandb.ai/dsta_unilu/cnn_digits?workspace=user-florian-goldinger)

We parameterized the scripts with the following parameters and conducted different experiments:

```
wandb.config.epochs
wandb.config.batch_size 
wandb.config.num_filters 
wandb.config.num_layers 
wandb.config.activation_fun 
```

Accordingly the loss and accuracy was tracked together with all the chosen parameters. With the code below the results have been logged to W&B: 

```
# Log the test loss and accuracy

wandb.log({"test_loss": score[0], "test_accuracy": score[1]})

# Log all parameters
wandb.log({"epochs": wandb.config.epochs})
wandb.log({"batch_size": wandb.config.batch_size})
wandb.log({"num_filters": wandb.config.num_filters})
wandb.log({"num_layers": wandb.config.num_layers})
wandb.log({"activation_function": wandb.config.activation_fun})
```

As described we have not done any optimization but only tried some different parameters and saved the result. Which are now accessible on the W&B platform. 

```
To save the predictions and the ground_truth the following code was added. The numpy arrays are needed for the Task 3, to graphically display the results:```
# Save the ground truth and the predictions for further graphical analysis
ground_truth = np.argmax(y_test, axis=1)
predictions = predict_classes(loaded_model, x_test)

np.save("ground_truth.npy", ground_truth)
np.save("predictions.npy", predictions)
```

Additionally a log was created for the predictions, saving them as artifact on W&B:

```
# Log predictions 
artifact = wandb.Artifact('predictions', type='predictions')
artifact.add_file('predictions.npy')
wandb.log_artifact(artifact)
```

