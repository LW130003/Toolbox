import cv2

pil_image = Image.open(path)
image = np.asarray(pil_image)
image = cv2.imread(path)

(h, w) = image.shape[:2]
(b,g,r) = image[0,0] # OpenCV read image in BGR format

# Change pixel at (0,0) to red
image[0,0] = (0,0,255)

# Center of Image
(cX, cY) = (w//2, h//2)

# Slicing Image
# Recall the shape is hxwxc
tl = image[0:cY, 0:cX] # Top Left
tr = image[0:cY, cX:w]
br = image[cY:h, cX, w]
bl = image[cY:h, 0:cX]