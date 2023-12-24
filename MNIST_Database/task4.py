import psycopg2
import numpy as np
from tensorflow import keras
from mnist_database_utils import create_table, create_table_with_predictions, insert_images, insert_prediction
from mnist_database_utils import get_image_from_id, get_prediction_from_image_id
from image_binary_convertation import binary_to_training_array

model_path = '/usr/src/app/saved_model.keras'
#model_path = '../saved_model.keras'

# The id of my favourite image (from the train sample)
image_id = 1

# Connection parameters
host = 'db'
port = 5432
user = 'postgres'
password = 'mypassword'
database = 'milestone_3'
predictions_table = 'predictions'
input_table = 'input_data'


# Establish a connection to Server
conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database,
)
conn.autocommit = True
cursor = conn.cursor()

# Creating the input table, and inserting the image there
try:
    create_table(cursor, input_table)
    conn.commit()

except psycopg2.Error:
    print("The input data table might already exist, data is not going to be inserted.")

else:
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    insert_images(cursor, input_table, x_train[image_id - 1: image_id], y_train[image_id - 1: image_id],
                  is_train=True)
    image_binary, label, is_train = get_image_from_id(cursor, input_table, image_id)
    print("True label that is stored in the input table: ", label)
    conn.commit()

# Creating the predictions table, and inserting the prediction there
try:
    create_table_with_predictions(cursor, predictions_table)
    conn.commit()

except psycopg2.Error:
    print("The predictions table might already exist, data is not going to be inserted.")

else:
    image_binary, label, is_train = get_image_from_id(cursor, input_table, image_id)
    model = keras.models.load_model(model_path)
    image = binary_to_training_array(image_binary)
    prediction = np.argmax(model.predict(image), axis=1)
    insert_prediction(cursor, predictions_table, image_id, prediction)
    retrieved_prediction = get_prediction_from_image_id(cursor, predictions_table, image_id)
    print("Prediction stored in the predictions table: ", retrieved_prediction)
    conn.commit()
