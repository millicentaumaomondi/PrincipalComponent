# Principal Component Analysis
## Introduction

It is a dimensionality reduction technique used to simplify a large data set into a smaller set while still maintaining significant patterns and trends.

## Steps of Conducting PCA:

- Standardize the data.
- Compute the covariance matrix so as to identify the correlation between the variables.
- Compute the eigenvectors and eigenvalues of the covariance matrix to identify the principal components.
- Create a feature vector to decide which principal components to keep.
- Recast the data along the principal component axes.

## User Instructions

This repository has two .py files: pca.py and pca_main.py

## 1. pca.py

Here, we build a class PCA where we will put some functions to aid in the PCA analysis computation.
- the fit function where where we will follow the above steps.
    - standardizing data
    - calculating the covarince matrix
    -  getting the eigen values and vectors.
    -  sorting the eigen vectors based on the eigen values.
    -  storing the first n_components.
 
- the transform function which returns the dot product of the variables and the transpose of the components.

## main_pca.py

- Here we call the PCA class function from the pca.py file.
- We import the necessary Python libraries.
- We then loaded the iris data set.
- Finally, called the PCA function with 2 comonents to get our results.
