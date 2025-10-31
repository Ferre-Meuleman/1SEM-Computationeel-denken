from PIL import Image
import numpy as np
""""De afmetingen van het beeld vergroten. Vervolgens worden de randen opgevuld, en tenslotte wordt het beeld gekopieerd 
van de oorspronkelijke matrices naar de nieuwe."""

# Open image
input_image = Image.open("Landschap1.jpg")
img_array = np.array(input_image)

# Get image dimensions
height, width, channels = img_array.shape

# Create output array
output_array = np.full((height + 10, width + 10, channels), (0, 255, 0), dtype=np.uint8)

# Copy original image to output array
for i in range(height):
    for j in range(width):
        for c in range(channels):
            output_array[i + 5][j + 5][c] = img_array[i][j][c]

# Convert output array to image
output_image = Image.fromarray(output_array)
output_image.show()
