import numpy as np
import pickle

from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix


with open('data/training_images.pickle', 'rb') as f:
    images = pickle.load(f)

with open('data/training_labels.pickle', 'rb') as f:
    labels = pickle.load(f)

def transform_labels(x):
    arr = np.zeros(10)
    arr[int(x)] = 1
    return arr

labels = np.array(list(map(transform_labels, labels)), dtype=int)

mlp = MLPClassifier(hidden_layer_sizes=(16, 16), max_iter=1000)
mlp.fit(images, labels)

with open('model/mlp_own_data.pickle', 'wb') as f:
    pickle.dump(mlp, f, pickle.HIGHEST_PROTOCOL)