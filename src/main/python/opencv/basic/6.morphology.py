
# Morphological operations are simple transformations applied to 
# binary or grasycale images.

# More specifically, we apply morphological operations to increase
# the size of objects in images as well as decrease them.

# We can also utilize morphological operations to close gaps between
# objects as well as open them.

# Morphological operations "probe" an image with a structuring element.
# This structuring element defines the neighborhood to be examined around
# each pixel. And based on the given operation and the size of the 
# structuring elementwe are able to adjust our output image.

# Morphological operations are image processing transformation applied to either
# grayscale or binary images. 
# These operations require a structuring element, which is used to define the 
# neighborhood of pixels the operation is applied to.

# Morphological operations are commonly used as pre-processing steps to more
# powerful computer vision solutions such as OCR, 
# Automatic Number Plate Recognition (ANPR), and barcode detection.

# While these techniques are simple, they are actually extremely powerful and tend
# to be highly useful when pre-processing your data.

# # =========================================
# # Structuring Element
# ```python
# cv2.getStructuringElement
# ```

# =========================================
# Erosion
# - Erosion works by defining a structuring element and then sliding 
# this structuring element from left-to-right and top-to-bottom across the input image.
# - A foreground pixel in the input image will be kept only if ALL pixels inside the 
# structuring element are > 0. Otherwise, the pixels are set to 0 (i.e. background)
# - Erosion is useful for removing small blobs in an image or disconnecting two connected objects.

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# apply a series of erosions
for i in range(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
    cv2.waitKey(0)

# =========================================
# Dilation
# - Opposite of dilation
# - Dilation incrase the size of foreground object and are especially useful for joining
# broken parts of an image together.
# - A center pixel p of the structuring element is set to white if ANY pixel in the strucutring element is > 0.
# apply a series of dilations
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    cv2.waitKey(0)

# =========================================
# Opening
# - An Opening is an erosion followed by a dilation
# - Performing an opening operation allows us to remove small blobs from an image:
#   - First an erosion is applied to remove small blobs, 
#   - Then, a dilation is applied to regrow the size of the original object.

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)

# =========================================
# Closing
# - The exact opposite to aan opening
# - Dilation followed by an erosion
# - Closing is used to close holes inside of objects or 
#   connected components together.
# loop over the kernels and apply a "closing" operation to the image
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

# =========================================
# Morphological Gradient
# - A morphological gradient is the differencce between the dilation and erosion.
# - It is useful for determining the outline of a particular object of an image

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)
    cv2.waitKey(0)

# =========================================
# Top Hat
# - A Top Hat is the difference between the original (grayscale / single channel) input image and the opening.
# - A top hat operation is sued to reveal bright regions of an image on dark backgrounds
# - We can apply morphological operations to grayscale image as well.
# - Top hat/White hat and black hat are more suited for grayscale images rather than binary ones.
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# =========================================
# Black hat
# - The Black Hat operation is the difference between the closing of the input image and the input image itself.
# - Opposite of White Hat/Top Hat
# - Black hat is applied to reveal the dark regions against light background.
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
