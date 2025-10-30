# importeer libraries 
from PIL import Image
import numpy as np 

# ====== Invoerparameters ======
hoogte = 600
breedte = 900

# Eerste cirkel (rood)
x1, y1, r1 = 360, 450, 120

# Tweede cirkel (groen)
x2, y2, r2 = 270, 540, 180

# ====== Achtergrond (grijs) ======
# Let op: volgorde is (hoogte, breedte)
r_out = np.ones((hoogte, breedte)) * 128
g_out = np.ones((hoogte, breedte)) * 128
b_out = np.ones((hoogte, breedte)) * 128

# ====== Maak raster van coördinaten ======
# X = kolomindex (0 links → breedte-1 rechts)
# Y = rijindex (0 boven → hoogte-1 onder)
Y, X = np.meshgrid(np.arange(hoogte), np.arange(breedte), indexing='ij')

# ====== FIX: oorsprong linksonder ======
# Draai y-as om zodat y=0 onderaan ligt
Y_cart = hoogte - 1 - Y

# ====== Bereken afstand tot elk middelpunt ======
dist1 = np.sqrt((X - x1)**2 + (Y_cart - y1)**2)
dist2 = np.sqrt((X - x2)**2 + (Y_cart - y2)**2)

# ====== Maskers voor cirkels ======
mask1 = dist1 <= r1
mask2 = dist2 <= r2
mask_both = mask1 & mask2

# ====== Kleuren toepassen ======
# Eerste cirkel: rood
r_out[mask1] = 255
g_out[mask1] = 0
b_out[mask1] = 0

# Tweede cirkel: groen
r_out[mask2] = 0
g_out[mask2] = 255
b_out[mask2] = 0

# Intersectie: geel (rood + groen)
r_out[mask_both] = 255
g_out[mask_both] = 255
b_out[mask_both] = 0

# ====== Converteer naar afbeelding ======
r_img = Image.fromarray(np.uint8(r_out))
g_img = Image.fromarray(np.uint8(g_out))
b_img = Image.fromarray(np.uint8(b_out))
output_im = Image.merge("RGB", (r_img, g_img, b_img))

# ====== Toon resultaat ======
output_im.show()
