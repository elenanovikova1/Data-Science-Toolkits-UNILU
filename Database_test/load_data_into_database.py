import psycopg2
import numpy as np
from keras.datasets import mnist
import keras

# Function to get MNIST data
def get_data():
    num_classes = 10
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.astype("float32") / 255
    x_test = x_test.astype("float32") / 255
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)
    return (x_train, y_train), (x_test, y_test)

# Connection parameters
host = 'localhost'
port = 5432
user = 'postgres'
password = 'mypassword'
default_db = 'mydatabase'

# Establish a connection to the database
conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=default_db,
)

cursor = conn.cursor()

# Create the new table for training data
cursor.execute("""
    CREATE TABLE mnist_binary_train (
        id SERIAL PRIMARY KEY,
        x_train BYTEA,
        y_train BYTEA
    );
""")

# Create the new table for testing data
cursor.execute("""
    CREATE TABLE mnist_binary_test (
        id SERIAL PRIMARY KEY,
        x_test BYTEA,
        y_test BYTEA
    );
""")

# Get the MNIST data
(x_train, y_train), (x_test, y_test) = get_data()

# Insert each row from the training data into the training table
for i in range(len(x_train)):
    x_train_bytes = psycopg2.Binary(np.ascontiguousarray(x_train[i]).tobytes())
    y_train_bytes = psycopg2.Binary(np.ascontiguousarray(y_train[i]).tobytes())

    cursor.execute("""
        INSERT INTO mnist_binary_train (x_train, y_train)
        VALUES (%s, %s);
    """, (x_train_bytes, y_train_bytes))

# Insert each row from the testing data into the testing table
for i in range(len(x_test)):
    x_test_bytes = psycopg2.Binary(np.ascontiguousarray(x_test[i]).tobytes())
    y_test_bytes = psycopg2.Binary(np.ascontiguousarray(y_test[i]).tobytes())

    cursor.execute("""
        INSERT INTO mnist_binary_test (x_test, y_test)
        VALUES (%s, %s);
    """, (x_test_bytes, y_test_bytes))

conn.commit()

cursor.close()
conn.close()