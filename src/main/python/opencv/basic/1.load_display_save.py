import cv2
import requests
from PIL import Image

# Load 
image = cv2.imread(args["image"])
h, w, c = image.shape # height, width, channel

## Load from web
pil_image = Image.open(requests.get(url, stream=True).raw)

# Show
cv2.imshow("Image", image)
cv2.waitKey(0)

display(pil_image) # Pil Image

## Display grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)

# Save
cv2.imwrite("newimage.jpg", image)
pil_image.save("newimage.jpg")