from PIL import Image
import numpy as np

# Open image
input_image = Image.open("Landschap1.jpg")

img_array = np.array(input_image)

mirrored_array = img_array[:, ::-1]
mirrored_array = mirrored_array[::-1, :]
mirrored_image = Image.fromarray(mirrored_array)
mirrored_image.show()