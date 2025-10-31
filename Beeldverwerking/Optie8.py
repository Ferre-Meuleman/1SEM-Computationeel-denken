from PIL import Image
import numpy as np

# Open image
input_image = Image.open("Landschap1.jpg")
img_array = np.array(input_image)

# Get image dimensions
height, width, channels = img_array.shape

# Create output array
output_array = np.zeros((height, width, channels), dtype=np.uint8)

# Apply blur effect
for i in range(1, height - 1):
    for j in range(1, width - 1):
        for c in range(channels):
            # Calculate the average of the 3x3 neighborhood
            neighborhood = img_array[i-1:i+2, j-1:j+2, c]
            output_array[i, j, c] = np.mean(neighborhood)

# Convert output array to image
output_image = Image.fromarray(output_array)
output_image.show()
