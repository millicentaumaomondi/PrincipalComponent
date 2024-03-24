from pca import PCA

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
X = iris['data']
y = iris['target']


n_samples, n_features = X.shape

print('Number of samples:', n_samples)
print('Number of features:', n_features)

pca = PCA(n_component=2)

def main():
    if __name__ == "__main__":main()

