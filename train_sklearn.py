import numpy as np
from mnist import MNIST
import pickle

from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix


mndata = MNIST('data')
images_train, labels_train = mndata.load_training()

images_train, labels_train = images_train[:30000], labels_train[:30000]

def transform_labels(x):
    arr = np.zeros(10)
    arr[x] = 1
    return arr

labels_train = np.array(list(map(transform_labels, labels_train)))

mlp = MLPClassifier(hidden_layer_sizes=(16, 16), max_iter=1000)  
mlp.fit(images_train, labels_train)


with open('model/mlp.pickle', 'wb') as f:
    pickle.dump(mlp, f, pickle.HIGHEST_PROTOCOL)
