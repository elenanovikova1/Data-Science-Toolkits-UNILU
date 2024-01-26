import requests
import json
import base64
from tensorflow import keras
import numpy as np

from PIL import Image

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

image_file_name = 'image0.png'
#first_image = Image.fromarray(x_train[0])
#first_image.save(image_file_name, 'PNG')

with open(image_file_name, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

data = {"image": encoded_string}

url = "http://localhost:5001/predict"


response = requests.post(url, json=data)

print(response.json())

