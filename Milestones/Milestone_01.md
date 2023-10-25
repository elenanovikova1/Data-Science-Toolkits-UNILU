##Milestone 01

###Question 01 

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
