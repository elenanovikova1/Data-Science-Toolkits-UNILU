##Milestone 1 

###Question 1 

## Problem and Dataset Description

1. **About the Dataset**: The dataset consists of 70,000 images, with 
60,000 samples in the training set and 10,000 samples in the test set. 
Each image depicts a handwritten digit, and it is labeled to indicate 
which digit is shown in the picture.

2. **Labels Format**: Each image is associated with a label. These labels 
are structured as vectors with 10 entries. Notably, all entries in each 
label vector are zero except for one entry, which is set to one. The 
position of this non-zero entry corresponds to the digit represented by 
the image. For instance, a picture of the digit seven would have a label 
vector like this: `(0;0;0;0;0;0;1;0;0;0)`.

3. **Classification Problem**: The objective of this dataset is to train a 
classifier that can predict which digit is depicted in each image. With 10 
different digits to choose from (0 to 9), this problem is classified as a 
"classification problem." Classification problems deal with predicting 
discrete and finite values, which are the digit labels in this context.

### Problem Type: Classification

- **Classification vs. Regression**: In machine learning, classification 
problems involve predicting a discrete label or category (in this case, 
the digit shown in the image). Regression problems, on the other hand, aim 
to estimate an unknown function based on observed function values, which 
typically involve continuous data. In this context, the problem falls 
under classification since the objective is to classify images into 
distinct categories (digits), each represented by a label.

### Dataset Characteristics

- **Image Characteristics**: The images in the dataset are 28x28 pixels in 
size. This means that each image consists of a grid of 28x28 pixels with 
varying shades, and the grayscale value of each pixel likely represents 
the darkness or lightness of that specific area. For example, if a pixel 
is very dark, it might be close to black, and if it's very light, it might 
be closer to white.

- **Data Structure**: The training dataset is labeled with the correct 
digit, and the algorithm uses this labeled data to learn how to recognize 
and classify these digits. The goal is to build a machine learning model 
that can predict the correct digit when given an image of a handwritten 
number.

This summary should help provide an overview of the dataset, the problem 
type, and the specific characteristics of the data. If there are any 
additional details available about the dataset, it's a good practice to 
include them, but this summary covers the essential aspects for 
understanding the problem and dataset.
