from PIL import Image

img1 = Image.open("./Capture the flag/Challenge_4/boodschap_deel_A.jpg").convert("L")  # 'L' = grayscale
img2 = Image.open("./Capture the flag/Challenge_4/boodschap_deel_B.jpg").convert("L")

if img1.size != img2.size:
    raise ValueError("Afbeeldingen hebben niet dezelfde dimensies!")

result = Image.new("1", img1.size)  # "1" = zwart/wit

pixels1 = img1.load()
pixels2 = img2.load()
result_pixels = result.load()

for x in range(img1.width):
    for y in range(img1.height):
        if pixels1[x, y] == pixels2[x, y]:
            result_pixels[x, y] = 1  # wit
        else:
            result_pixels[x, y] = 0  # zwart

result.save("result.png")

# (Optioneel) Toon de afbeelding
result.show()
