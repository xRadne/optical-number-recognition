from flask import Flask, render_template, request, Response
import numpy as np
import json
import pickle
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
app = Flask(__name__)

with open('../model/mlp.pickle', 'rb') as f:
    mlp = pickle.load(f)

@app.route('/')
def draw():
    return render_template('draw.html')

@app.route('/classify', methods=['POST'])
def classify():
    image = json.loads(request.data)
    image = np.array(image).reshape(1, -1)
    prediction = mlp.predict(image)[0]

    prediction = prediction.argmax(0)

    print(f'Prediction: {prediction}', flush=True)
    # image = np.split(image, 28)
    # plt.imshow(image, 'binary')
    # plt.show()
    return Response(f"It looks like a {prediction}")

if __name__ == '__main__':
    app.run(debug=True)