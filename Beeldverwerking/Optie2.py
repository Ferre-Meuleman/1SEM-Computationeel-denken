# importeer libraries 
from PIL import Image 
import math  
import numpy as np 
 
# converteer een ingelezen afbeelding naar drie matrices 
input_image = Image.open("Landschap1.jpg") 
r_image_in, g_image_in, b_image_in = input_image.split() 
r_in = np.uint32(np.array(r_image_in)) 
g_in = np.uint32(np.array(g_image_in)) 
b_in = np.uint32(np.array(b_image_in)) 
 
# hier komen de matrixbewerkingen !!! 
r_out = np.zeros((r_in.shape[0], r_in.shape[1])) 
g_out = np.zeros((g_in.shape[0], g_in.shape[1])) 
b_out = np.zeros((b_in.shape[0], g_in.shape[1])) 

for i in range(r_in.shape[0]): 
    for j in range(r_in.shape[1]): 
            r_out[i][j] = 255 - r_in[i][j] 
            g_out[i][j] = 255 - g_in[i][j] 
            b_out[i][j] = 255 - b_in[i][j] 
 
# converteer drie matrices terug naar een afbeelding 
r_image_out = Image.fromarray(np.uint8(r_out)) 
g_image_out = Image.fromarray(np.uint8(g_out)) 
b_image_out = Image.fromarray(np.uint8(b_out)) 
output_im = Image.merge("RGB", (r_image_out, g_image_out, b_image_out)) 
output_im.show()