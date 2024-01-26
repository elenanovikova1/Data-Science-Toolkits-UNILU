from image_binary_convertation import image_to_binary, binary_to_image


def create_table(cursor, table_name):
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            image_binary BYTEA,
            label INTEGER
        );
    """)


def insert_image(cursor, table_name, image_binary, label):
    insert_sql = f"""
    INSERT INTO {table_name} (image_binary, label)
    VALUES (%s, %s)
    """
    cursor.execute(insert_sql, (image_binary, int(label)))


def insert_images(cursor, table_name, images, labels):
    for image, label in zip(images, labels):
        binary_data = image_to_binary(image)
        insert_image(cursor, table_name, binary_data, label)


def get_image_from_id(cursor, table_name, image_id):
    select_sql = f"SELECT image_binary, label, is_train FROM {table_name} WHERE id = %s;"
    cursor.execute(select_sql, (image_id,))
    return cursor.fetchone()


def show_image_by_id(cursor, table_name, image_id):
    image_binary, label = get_image_from_id(cursor, table_name, image_id)
    image = binary_to_image(image_binary)
    image.show()
    print(f"Label: {label}")
