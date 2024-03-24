import numpy as np
class PCA:
  def __init__(self,n_component):
    self.n_component =n_component
    self.component = None
    self.mean = None
    self.std = None

  def fit(self,X):
    #Standardise the dataset
    self.mean = 1/(X.shape[0]) * np.sum(X,axis =0)
    self.std = (1/(X.shape[0]-1)*(np.sum((X-mean(X))**2, axis = 0)))**0.5

    X_std = (X - self.mean)/self.std

    #Calculate covariance
    cov = (1/(X.shape[0]-1))*X.T@X

    # Getting the eigen values and vectors
    eigen_values, eigen_vectors = np.linalg.eig(covariance(X_std))

    #Sorting the eigen vectors based on eigen values
    idx = np.array([np.abs(i) for i in eigen_values]).argsort()[::-1]
    eigen_values_sorted = eigen_values[idx]
    eigen_vectors_sorted = eigen_vectors.T[:,idx]

    # Store the first n_components eigenvectors
    self.components = eigen_vectors_sorted

    #Store the first n_components
    explained_variance = [(i / sum(eigen_values))*100 for i in eigen_values_sorted]
    explained_variance = np.round(explained_variance, 2)
    cum_explained_variance = np.cumsum(explained_variance)

  def transform(self,X):
    X = (X - self.mean)/self.std

    return (np.dot(X,self.components.T))