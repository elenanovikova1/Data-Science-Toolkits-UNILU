# Milestone 04

## Task 1

### What is Experiment Management and why is it important?

Experiment Managements refers to the systematic organisation and tracking of experiments during the development and training of predictive models (in our case a convolutional network). The model is based on a multitude of parameters (e.g. data used, preprocessing steps, model architecture, hyperparameters). Experiments should identify the causal effect of the change of one parameter (keeping the other ones fix) on the outcome/prediction. 

Given the diversity of parameters involved in these experiments, it can be challenging to keep track of all the variations. Especially in a collaborative software project involving multiple team members, a systematic approach to documenting experiments becomes crucial. This systematic approach ensures that the organization can maintain knowledge about the experiments conducted, allowing team members to understand and build upon each other's work.

### What is a Metric in ML?

A metric in machine learning is a quantitative measure used to assess the performance of a model. It provides a summarized numerical evaluation of how well the model performs on a specific task, given a set of parameters.

## What is Precision and Recall? Why is there often a Trade-off between them?

*Precision* is the ratio of true positives to the sum of true positives and false positives. In the example of spam, it measures how many of the emails detected as spam are actually spam. 
*Recall* is the ratio of true positives to the sum of true positives and false negatives. For spam, it measures on how much of the actual spam I found. Did I detect all of them. 

There is a trade-off between precision and recall because improving one can lead to a deterioration of the other metric. It depends on the context on what is more important.

For example cancer diagnosis, where the goal is to detect all patients actually suffering from cancer, recall becomes crucial. It's more acceptable to have a few false positives (patients without cancer being incorrectly identified) if it means capturing all or most of the true positive cases (patients with cancer).

On the other hand, in the context of spam detection, where the goal is to avoid marking legitimate emails as spam, precision becomes more critical. Accepting a few false negatives (spam emails not detected) may be more tolerable if it means minimizing the number of false positives (legitimate emails incorrectly marked as spam).

## What is AUROC Metric?

AUROC is the abbreviation for Area Under the Receiver Operating Characteristic curve. 

The Receiver Operating Characteristic curve plots the true Positive rate against the False positive rate in a classification model. It plots the trade-off between TP and FP. 
The AUROC therefore measures the are under this curve for different thresholds. A higher AUROC value indicates better performance.

## What is a Confusion Matrix?

A confusion matrix is a table used to evaluate the performance of a classification model. 
In general it compares the actual vs. the predicted class and shows the following:

- TP (True Positive)
- FP (False Positive)
- TN (True Negative)
- FN (False Negative)
