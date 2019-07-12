import numpy as np
import pickle

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

from matplotlib import pyplot as plt

def transform_labels(x):
    arr = np.zeros(10)
    arr[int(x)] = 1
    return arr

def show_feature(feature):
    img = np.array_split(feature, 28)
    img = np.array(img)
    plt.matshow(img)
    plt.show()

def evaluate_model(model, features, labels):
    labels = np.array(list(map(transform_labels, labels)))
    predictions = model.predict(features)
    predictions = np.argmax(predictions, 1)
    labels = np.argmax(labels, 1)

    print(classification_report(labels, predictions))
    print(confusion_matrix(labels, predictions))


with open('model/mlp_own_data.pickle', 'rb') as f:
    mlp = pickle.load(f)

with open('data/training_images.pickle', 'rb') as f:
    images = pickle.load(f)

with open('data/training_labels.pickle', 'rb') as f:
    labels = pickle.load(f)

print("Evaluate training data")
evaluate_model(mlp, images, labels)

with open('data/test_images.pickle', 'rb') as f:
    images = pickle.load(f)

with open('data/test_labels.pickle', 'rb') as f:
    labels = pickle.load(f)

print("Evaluate test data")
evaluate_model(mlp, images, labels)