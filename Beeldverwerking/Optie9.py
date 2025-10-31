from PIL import Image
import numpy as np

# Open image
input_image = Image.open("Landschap1.jpg")
img_array = np.array(input_image)

# Get image dimensions
height, width, channels = img_array.shape

# Create output array
output_array = np.zeros((height //2, width //2, channels), dtype=np.uint8)

# Reduce image dimensions by averaging 2x2 pixel blocks
for i in range(0, height, 2):
    for j in range(0, width, 2):
        for c in range(channels):
            # Calculate the average of the 2x2 block
            block = img_array[i:i+2, j:j+2, c]
            output_array[i //2, j //2, c] = np.mean(block)

# Convert output array to image
output_image = Image.fromarray(output_array)
output_image.show()
