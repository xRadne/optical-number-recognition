import numpy as np
import pickle
import json
from PIL import Image
import PIL.ImageOps
import matplotlib.pyplot as plt

def expand_data(data):
    return [(val, val, val) for val in data]

def contract_data(data):
    return [val[0] for val in data]

def translate_up(steps, data):
    return_data = list(data)
    return_data.extend([0]*(28*steps))
    return return_data[28*steps:]

def translate_down(steps, data):
    return_data = list(data)
    return_data[0:0] = [0] * (28 * steps)
    return return_data[:-28*steps]

def translate_right(steps, data):
    return_data = list(data)
    return_data[0:0] = [0] * steps
    for row in range(1, 28):
        return_data[row*28:row*28+steps] = [0] * steps
    del return_data[-steps:]
    return return_data

def translate_left(steps, data):
    return_data = list(data)
    del return_data[0:steps]
    for row in range(1, 28):
        return_data[row*28 - steps:row*28] = [0] * steps
    return_data.extend([0]*steps)
    return return_data

def translate_image(x, y, data):
    if x > 0:
        data = translate_right(x, data)
    elif x < 0:
        data = translate_left(-x, data)
    
    if y > 0:
        data = translate_up(y, data)
    elif y < 0:
        data = translate_down(-y, data)

    return data

with open('images.json', 'r') as f:
    images = json.load(f)

with open('labels.json', 'r') as f:
    labels = json.load(f)

#Select and save test data
test_set_proportion = 0.15
test_set_size = int(len(images) * test_set_proportion)

rng_state = np.random.get_state()
np.random.shuffle(images)
np.random.set_state(rng_state)
np.random.shuffle(labels)

test_images = np.array(images[:test_set_size], dtype=float)
test_labels = np.array(labels[:test_set_size], dtype=int)

test_images /= 255

with open('test_images.pickle', 'wb') as f:
    pickle.dump(test_images, f, pickle.HIGHEST_PROTOCOL)

with open('test_labels.pickle', 'wb') as f:
    pickle.dump(test_labels, f, pickle.HIGHEST_PROTOCOL)

training_images = images[test_set_size:]
training_labels = labels[test_set_size:]

#Multiply the traning data by rotating and translating the samples
rotations = [-20, 0, 20]
translations = list(range(-3, 4))

number_of_samples = len(training_images) * len(rotations) * len(translations) ** 2

dataset_images = np.empty(shape=(number_of_samples, 28 * 28), dtype=float)
dataset_labels = np.empty(shape=(number_of_samples), dtype=int)

im = Image.new("L", (28, 28), color=0)

index = 0
for image, label in zip(training_images, training_labels):
    im.putdata(image)
    for angle in rotations:
        im_rotated = im.rotate(angle)
        imdata = list(im_rotated.getdata())
        for x in translations:
            for y in translations:
                data = np.array(translate_image(x, y, imdata))
                data = data / 255
                dataset_images[index] = data
                dataset_labels[index] = int(label)
                index += 1

with open('training_images.pickle', 'wb') as f:
    pickle.dump(dataset_images, f, pickle.HIGHEST_PROTOCOL)

with open('training_labels.pickle', 'wb') as f:
    pickle.dump(dataset_labels, f, pickle.HIGHEST_PROTOCOL)