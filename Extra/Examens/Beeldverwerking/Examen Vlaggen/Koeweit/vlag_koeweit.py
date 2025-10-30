from PIL import Image
import numpy as np

green = [54, 129, 73]
white = [255, 255, 255]
red = [252, 29, 0]
black = [0, 0, 0]

height = int(input("Geef de hoogte op: "))
length = 0
while not (1.4 * height <= length <= 2.5 * height):
    length = int(input(f"Geef de lengte op tussen {1.4 * height:.1f} - {2.5 * height:.1f}: "))

stripe = height // 3
img = np.zeros((height, length, 3), dtype=np.uint8)

i = 0
while i < height:
    if i < stripe:
        split = i
        color = green
        
    elif i < 2 * stripe:
        split = stripe
        color = white
        
    else:
        split = height - i
        color = red

    if split > 0:
        img[i, :split] = black
    img[i, split:] = color
    i += 1

Image.fromarray(img).show()