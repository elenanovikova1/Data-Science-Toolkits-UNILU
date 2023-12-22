import psycopg2
import numpy as np
from keras.datasets import mnist
import keras

def load_mnist_data():
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

    # Load training data from the database
    cursor.execute("""
        SELECT x_train, y_train
        FROM mnist_binary_train;
    """)
    train_data = cursor.fetchall()

    # Load testing data from the database
    cursor.execute("""
        SELECT x_test, y_test
        FROM mnist_binary_test;
    """)
    test_data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Convert the data back to numpy arrays
    x_train = [np.frombuffer(row[0], dtype=np.float32) for row in train_data]
    y_train = [np.frombuffer(row[1], dtype=np.float32) for row in train_data]
    x_test = [np.frombuffer(row[0], dtype=np.float32) for row in test_data]
    y_test = [np.frombuffer(row[1], dtype=np.float32) for row in test_data]

    # Reshape the data
    x_train = np.array(x_train).reshape(-1, 28, 28, 1)
    y_train = np.array(y_train).reshape(-1, 10)
    x_test = np.array(x_test).reshape(-1, 28, 28, 1)
    y_test = np.array(y_test).reshape(-1, 10)

    return x_train, y_train, x_test, y_test