from image_binary_convertation import image_to_binary, binary_to_image

def create_table(cursor, table_name):
    cursor.execute(f"""
        CREATE TABLE {table_name} (
            id SERIAL PRIMARY KEY,
            image_binary BYTEA,
            label INTEGER,
            is_train BOOLEAN
        );
    """)

def create_table_with_predictions(cursor, table_name):
    cursor.execute(f"""
        CREATE TABLE {table_name} (
            id SERIAL PRIMARY KEY,
            input_data_id INTEGER REFERENCES input_data(id),
            prediction INTEGER
        );
    """)

def insert_image(cursor, table_name, image_binary, label, is_train):
    insert_sql = f"""
    INSERT INTO {table_name} (image_binary, label, is_train)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_sql, (image_binary, int(label), is_train))

def insert_images(cursor, table_name, images, labels, is_train):
    for image, label in zip(images, labels):
        binary_data = image_to_binary(image)
        insert_image(cursor, table_name, binary_data, label, is_train)

def get_image_from_id(cursor, table_name, image_id):
    select_sql = f"SELECT image_binary, label, is_train FROM {table_name} WHERE id = %s;"
    cursor.execute(select_sql, (image_id,))
    return cursor.fetchone()

def show_image_by_id(cursor, table_name, image_id):
    image_binary, label, is_train = get_image_from_id(cursor, table_name, image_id)
    image = binary_to_image(image_binary)
    image.show()
    print(f"Label: {label}")
    if is_train:
        print("The image is from the train dataset.")
    else:
        print("The image is from the test dataset.")

def insert_prediction(cursor, table_name, image_id, prediction):
    insert_sql = f"""
        INSERT INTO {table_name} (input_data_id, prediction)
        VALUES (%s, %s)
        """
    cursor.execute(insert_sql, (image_id, int(prediction)))

def get_prediction_from_image_id(cursor, table_name, image_id):
    select_sql = f"SELECT prediction FROM {table_name} WHERE input_data_id = %s;"
    cursor.execute(select_sql, (image_id,))
    return cursor.fetchone()[0]

