from PIL import Image
import numpy as np

# Open image
input_image = Image.open("Landschap1.jpg")

img_array = np.array(input_image)

rotated_image = input_image.rotate(45, expand=True)
rotated_image.show()