from PIL import Image
import numpy as np

def edge_detection(img_path, threshold=None, save_path=None):

    img = Image.open(img_path).convert("RGB")
    arr = np.array(img, dtype=float)
    H, W, C = arr.shape


    Sx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=float)

    Sy = np.array([[-1, -2, -1],
                   [ 0,  0,  0],
                   [ 1,  2,  1]], dtype=float)

    edges = np.zeros_like(arr)

    for k in range(C):
        for i in range(1, H - 1):
            for j in range(1, W - 1):
                region = arr[i - 1:i + 2, j - 1:j + 2, k]
                gx = np.sum(Sx * region)
                gy = np.sum(Sy * region)
                edges[i, j, k] = np.sqrt(gx**2 + gy**2)

    edges = np.clip(edges, 0, 255)

    if threshold is not None:
        edges = np.where(edges > threshold, 255, 0)

    result = Image.fromarray(edges.astype(np.uint8))

    if save_path:
        result.save(save_path)
    return result


img = edge_detection("Landschap1.jpg")
img.show()

img_thresh = edge_detection("Landschap1.jpg", threshold=100)
img_thresh.show()
