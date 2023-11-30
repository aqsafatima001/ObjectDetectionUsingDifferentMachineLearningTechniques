# -*- coding: utf-8 -*-
"""K_nearest_Neighbour_ObjectDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12zahgVzyyPgyVVeycz7gTs0atanPU1b9

## **IMPORTING THE REQUIRED LIBRARIES**
"""

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from tensorflow.keras.datasets import cifar10
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

"""## **FLATTEN THE IMAGE**"""

X_train_flat = X_train.reshape((X_train.shape[0], -1))
X_test_flat = X_test.reshape((X_test.shape[0], -1))

"""## **STANDARDRIZE THE DATA**"""

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_flat)
X_test_scaled = scaler.transform(X_test_flat)

"""## **Hyperparameter tuning for the number of neighbors**"""

param_grid = {'n_neighbors': [3, 5, 7, 9]}  # Experiment with different values
knn = KNeighborsClassifier()
grid_search = GridSearchCV(knn, param_grid, cv=5)
grid_search.fit(X_train_scaled, y_train)

"""## **Get the best number of neighbors**"""

best_k = grid_search.best_params_['n_neighbors']
print(f"Best number of neighbors: {best_k}")

"""## **Initialize the K-NN model with the best parameter**"""

# Initialize the K-NN model with the best parameter
knn = KNeighborsClassifier(n_neighbors=best_k, metric='manhattan')
knn.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred_knn = knn.predict(X_test_scaled)

"""## **Calculate accuracy**"""

# Calculate accuracy
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"K-Nearest Neighbor Accuracy: {accuracy_knn}")