import numpy as np
from PIL import Image
import io

def image_to_binary(image_array):
    # Convert the numpy array to a PIL image
    image = Image.fromarray(np.uint8(image_array))
    binary_data = io.BytesIO()
    # Convert the image to binary format
    image.save(binary_data, format='PNG')
    img_byte_arr = binary_data.getvalue()
    return img_byte_arr

# Convert binary back to image for retrieval
def binary_to_image(binary_data):
    return Image.open(io.BytesIO(binary_data))

def binary_to_training_array(binary_data):
    image = binary_to_image(binary_data)
    array = np.array(image)
    array = array.astype("float32") / 255
    array = np.expand_dims(array, -1)
    return array
