import numpy as np
from mnist import MNIST
import pickle

from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix


mndata = MNIST('MNIST_Dataset')
images_train, labels_train = mndata.load_training()
images_test, labels_test = mndata.load_testing()

images_train, labels_train = images_train[:10000], labels_train[:10000]
images_test, labels_test = images_test[:2000], labels_test[:2000]


def transform_labels(x):
    arr = np.zeros(10)
    arr[x] = 1
    return arr

labels_train = np.array(list(map(transform_labels, labels_train)))
labels_test = np.array(list(map(transform_labels, labels_test)))


scaler = preprocessing.StandardScaler()
scaler.fit(images_train)

images_train = scaler.transform(images_train)
images_test = scaler.transform(images_test)

mlp = MLPClassifier(hidden_layer_sizes=(16, 16), max_iter=1000)  
mlp.fit(images_train, labels_train)

predictions = mlp.predict(images_test)

print(classification_report(labels_test,predictions))


with open('model/mlp.pickle', 'wb') as f:
    pickle.dump(mlp, f, pickle.HIGHEST_PROTOCOL)
    print("The model was saved as 'model/mlp.pickle'")