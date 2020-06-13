from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np


# Load data by load_iris function from sklearn
iris = load_iris()

features = iris.data.T

sepal_length = features[0]
sepal_width = features[1]
petal_length = features[2]
pepal_width = features[3]

sepal_length_label = iris.feature_names[0]
sepal_width_label = iris.feature_names[1]
pepal_length_label = iris.feature_names[2]
pepal_width_label = iris.feature_names[3]

plt.scatter(sepal_length, sepal_width, c = iris.target)
plt.xlabel(sepal_length_label)
plt.ylabel(sepal_width_label)
plt.show()


#############
# Initialize lists
setosa_sepal_length = []
setosa_sepal_width = []
setosa_petal_length = []
setosa_petal_width = []
versicolor_sepal_length = []
versicolor_sepal_width = []
versicolor_petal_length = []
versicolor_petal_width = []
virginica_sepal_length = []
virginica_sepal_width = []
virginica_petal_length = []
virginica_petal_width = []
# put data into each list
