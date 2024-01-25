import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.metrics import confusion_matrix


import numpy as np

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

ground_truth_file_name = os.path.join(os.path.dirname(__file__), '..', 'wandb', 'ground_truth.npy')
ground_truth = np.load(ground_truth_file_name)


predictions_file_name = os.path.join(os.path.dirname(__file__), '..', 'wandb', 'predictions.npy')
predictions = np.load(predictions_file_name)



cm = confusion_matrix(ground_truth, predictions)

plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.show()