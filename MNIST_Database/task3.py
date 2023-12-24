import psycopg2
from tensorflow import keras
from mnist_database_utils import create_table, insert_images, show_image_by_id

# Number of images from train and test datasets insearted into the table
n_train_images = 10
n_test_images = 5
# The id of my favourite image
image_id = 1

# Connection parameters
host = 'localhost'
port = 5432
user = 'postgres'
password = 'mypassword'
database = 'mnist_database'
table_name = 'mnist_table'

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

try:
    # Create the new table with the columns: id, binary representation of images, the label,
    # and a boolean flag that indicates if the image is from train (value = True) or test (value = False) datasets.
    create_table(cursor, table_name)
    conn.commit()

except psycopg2.Error:
    print("The table might already exist, data is not going to be inserted.")

else:
    # Downloading train and test datasets
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # Inserting data (binary representation of images, labels, and train/test boolean flags) to the database
    insert_images(cursor, table_name, x_train[:n_train_images], y_train[:n_train_images], is_train=True)
    insert_images(cursor, table_name, x_test[:n_test_images], y_test[:n_test_images], is_train=False)
    conn.commit()

finally:
    show_image_by_id(cursor, table_name, image_id)

    # Closing the connection
    cursor.close()
    conn.close()
