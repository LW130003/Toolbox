import numpy as np
import cv2

# =========================================
# 1. Translation
# NOTE: Translating (shifting) an image is given by a NumPy matrix in
# the form:
#	[[1, 0, shiftX], [0, 1, shiftY]]
# You simply need to specify how many pixels you want to shift the image
# in the X and Y direction -- let's translate the image 25 pixels to the
# right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# now, let's shift the image 50 pixels to the left and 90 pixels up, we
# accomplish this using negative values
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# =========================================
# 2. Rotation
(h, w)  = image.shape[:2]
(cX, cY) = (w//2, h//2)

# Rotate 45 degrees CC
M = cv2.getRotationMatrix2D((cX,cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

# OpenCV provides the ability to 
# 1) scale, (i.e. resize) an image and 
# 2) provide an arbitrary rotation center to perform about

# =========================================
# 3. Resizing

# Taking care aspect ratio
# Given Height
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0]*r))

# Given Width
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# =========================================
# 4. Flipping

# Flip horizontal
flipped = cv2.flip(image, 1)

# Flip vertical
flipped = cv2.flip(image, 0)

# Flip the image a long both axies
flipped = cv2.flip(image, -1)

# =========================================
# 5. Crop
# Cropping an image is accomplished using simple Numpy array slices.
crop  = image[y0:y1, x0:x1]

# =========================================
# 6. Image Arithmetic

# In reality, image arithmetic is simply matrix addition (with an added caveat on data types)
# - Matrix addition = element-wise sum of matrix entries

# NumPy perform modulus arithmetic and "wrap around". 
# OpenCv, on the other hand, will perform clipping and ensure pixel values never fall outside the range [0,255]

# Images are NumPy arrays, stored as unsigned 8 bit integers --
# that the values of our pixels will be in range [0,255];
# When using functions like cv2.add and cv2.subtract, 
# values will be clipped to this range, even if the added or subtracted values
# fall outside the range of [0,255].

print("max of 255: {}".format(str(cv2.add(np.uint8([200]), np.uint8([100])))))
print("min of 0: {}".format(str(cv2.subtract(np.uint8([50]), np.uint8([100])))))
# max of 255: [[255]]
# min of 0: [[0]]

# NOTE: if you use NumPy arithmetic operations on these arrays, the value
# will be modulos (wrap around) instead of being  clipped to the [0, 255]
# range. This is important to keep in mind when working with images.
print("wrap around: {}".format(str(np.uint8([200]) + np.uint8([100]))))
print("wrap around: {}".format(str(np.uint8([50]) - np.uint8([100]))))
# wrap around: [44]
# wrap around: [206]
# let's increase the intensity of all pixels in our image by 100 -- we
# accomplish this by constructing a NumPy array that is the same size of
# our matrix (filled with ones) and the multiplying it by 100 to create an
# array filled with 100's, then we simply add the images together; notice
# how the image is "brighter"
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)

# similarly, we can subtract 50 from all pixels in our image and make it
# darker
M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)

# =========================================
# 7. Bitwise operations

# first, let's draw a rectangle
rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)

# secondly, let's draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)

# A bitwise 'AND' is only True when both rectangle and circle have
# a value that is 'ON'. Simply put, the bitwise_and function
# examines every pixel in rectangle and circle. If both pixels
# have a value greater than zero, that pixel is turned 'ON' (i.e
# set to 255 in the output image). If both pixels are not greater
# than zero, then the output pixel is left 'OFF' with a value of 0.
bitwiseAnd = cv2.bitwise_and(rectangle, circle)

# A bitwise 'OR' examines every pixel in rectangle and circle. If
# EITHER pixel in rectangle or circle is greater than zero, then
# the output pixel has a value of 255, otherwise it is 0.
bitwiseOr = cv2.bitwise_or(rectangle, circle)

# The bitwise 'XOR' is identical to the 'OR' function, with one
# exception: both rectangle and circle are not allowed to BOTH
# have values greater than 0.
bitwiseXor = cv2.bitwise_xor(rectangle, circle)

# Finally, the bitwise 'NOT' inverts the values of the pixels. Pixels
# with a value of 255 become 0, and pixels with a value of 0 become
# 255.
bitwiseNot = cv2.bitwise_not(circle)

# =========================================
# 8. Masking

# Rectangular Mask
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)

# Circular Mask
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (145, 200), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)

# =========================================
# 9. Splitting and Merging Channel

# Important to note that OpenCV stores an image as NumPy array with
# its channels in reverse order!
(B, G, R) = cv2.split(image)

# Merge the image back together again
merged = cv2.merge([B, G, R])

# Visualize each channel in color
# visualize each channel in color
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

#
