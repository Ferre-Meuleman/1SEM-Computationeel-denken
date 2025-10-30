from PIL import Image
import numpy as np

blue = [0, 32, 91]
white = [255, 255, 255]
red = [252, 29, 0]
black = [0, 0, 0]

height = int(input("Geef de hoogte op: "))
length = 0
while not (int(0.7272 * height) <= length <= int(1.375 * height)):
    length = int(input(f"Geef de lengte op tussen {0.7272 * height:.0f} - {1.375 * height:.0f}: "))


w_b_stripe = int(length * (2/22))

v_start = int(length * (7/22))
v_end = v_start + w_b_stripe

h_b_stripe = w_b_stripe
h_start = int(height/2 - h_b_stripe/2)
h_end = h_start + h_b_stripe

q1h = int(length * (6/22))
q2h = int(length * (10/22))

q1v = int(height * (6/16))
q3v = int(height * (10/16))

img = np.zeros((height, length, 3), dtype=np.uint8)

img[:, :, :] = white


img[:, v_start:v_end, :] = blue
img[h_start:h_end, :, :] = blue

img[:q1v, :q1h, :] = red
img[:q1v, q2h:, :] = red

img[q3v:, :q1h, :] = red
img[q3v:, q2h:, :] = red

Image.fromarray(img).show()