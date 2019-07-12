import numpy as np
from mnist import MNIST
import pickle

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix


mndata = MNIST('data')

images_test, labels_test = mndata.load_training()
images_test, labels_test = images_test[:30000], labels_test[:30000]


with open('model/mlp.pickle', 'rb') as f:
    mlp = pickle.load(f)

predictions = mlp.predict(images_test)
predictions = np.argmax(predictions, 1)
labels = np.array(labels_test)

print(classification_report(labels,predictions))
print(confusion_matrix(labels, predictions))
