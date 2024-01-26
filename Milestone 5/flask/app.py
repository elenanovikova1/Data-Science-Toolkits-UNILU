from flask import Flask, request, jsonify
import numpy as np
from tensorflow import keras
import os
import psycopg2
import base64
import io

from database_utils import create_table, insert_image
from image_binary_convertation import binary_to_training_array
from image_binary_convertation import binary_to_image, image_to_binary

host = 'db'
port = 5432
user = 'postgres'
password = 'mypassword'
database = 'milestone_5'
input_table = 'mnist_table'

conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database,
)
conn.autocommit = True
cursor = conn.cursor()

create_table(cursor, input_table)
conn.commit()

app = Flask(__name__)

model_file_name = 'saved_model.keras'
model = keras.models.load_model(model_file_name)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        image_binary = request.json['image']

        image_decoded = base64.b64decode(image_binary)
        image_array = binary_to_training_array(image_decoded)
        image_array = np.expand_dims(image_array, axis=0)

        prediction = np.argmax(model.predict(image_array), axis=1)

        insert_image(cursor, input_table, image_to_binary(np.array(binary_to_image(image_decoded))), prediction)

        return jsonify({'prediction': str(prediction)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
