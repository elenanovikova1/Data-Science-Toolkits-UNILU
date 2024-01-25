from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image provided by the user
image_path = 'milestone4task3_picture.jpeg'
image = Image.open(image_path)

# Convert the image into a NumPy array
image_array = np.array(image)

# Extracting the Red, Green, and Blue channels
red_channel = image_array[:,:,0]
green_channel = image_array[:,:,1]
blue_channel = image_array[:,:,2]

# Plotting histograms for each channel
plt.figure(figsize=(12, 4))

# Red Channel Histogram
plt.subplot(1, 3, 1)
plt.hist(red_channel.ravel(), bins=256, color='red', alpha=0.5)
plt.title('Red Channel Histogram')
plt.xlim([0, 256])

# Green Channel Histogram
plt.subplot(1, 3, 2)
plt.hist(green_channel.ravel(), bins=256, color='green', alpha=0.5)
plt.title('Green Channel Histogram')
plt.xlim([0, 256])

# Blue Channel Histogram
plt.subplot(1, 3, 3)
plt.hist(blue_channel.ravel(), bins=256, color='blue', alpha=0.5)
plt.title('Blue Channel Histogram')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()