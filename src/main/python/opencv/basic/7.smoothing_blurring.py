# =========================================
# Smoothing and Blurring is one of the most common pre-processing steps in 
# computer vision and image processing.

# By smoothing an image prior to applying techniques such as edge detection or 
# thresholding we are able to reduce the amount of high frequency content, such as 
# noise and edges (i.e. the "detail" of an image).

# While this may sound counter-intuitive, by reducing the detail of an image, we can
# more easily find objects that we are interested in.

# Furthermore, this allows us to focus on the larger structural objects in the image.

# - The Simple Average method is fast, but may not preserve edges in images.
# - The Gaussian blur is better at preserving edges, but is slightly slower than the average method.
# - The median filter is primarly used to reduce salt-and-pepper style noise as the median statistics is much 
#   more robust and less sensitive to outliers than other statistical methods such as the mean.
# - The bilateral filter preserves edges, but is substantially slower than the other methods.
#   The bilateral filtering also boast the most parameters to tune which can become a nuisance to tune correctly.

# - In general, it is recommended to start with a simple Gaussina blur to obtain a baseline and then going from there.

# =========================================
# Averaging
# Average filter - takes an area of pixel surrounding a central pixel, averages all these
# pixels together, and replaces the central pixel with the average.

# By taking the average of the region surrounding a pixel, we are smoothing it and 
# replacing it with the value of its local neighborhood. This allows us to reduce noise 
# and the level of detail, simply by relying on the average.

# We can use kernels for not only edge detection and gradients, but for averaging as well.

# Important rule: As the size of the kernel increases, so will the amount in which the image is blurred.
# Simply put: the larger your smoothing kernel is, the more blurred your image will look.

kernelSizes = [(3, 3), (9, 9), (15, 15)]

# loop over the kernel sizes and apply an "average" blur to the image
for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)

# =========================================
# Gaussian
# Gaussian Blurring is similar to average blurring, but instead of using a simple mean,
# we are now using weighted mean, where neighborhood pixels that are closer to the central
# pixel contribute more "weight" to the average.

# Gaussian Smoothing is used to remove noise that approximately follows a Gaussian distribution.

# The end result is that our image is less blurred, but more naturally blurred, 
# then using the average method.

# Futhermore, based on weighting we'll be able to preserve more of the edges in our image
# as compared to average smoothing.

# G(x) = 1/np.sqrt(2 \pi \sigma) e^-(x^2/2 sigma^2)
# G(x, y) = 1/\sqrt(2 \pi \sigma) e^-(x^2+y^2)/(2 sigma^2)

# In general, I tend to recommend starting with a simple Gaussian blur and 
# tuning your parameters as needed. 
# While the Gaussian blur is slightly slower than a simple average blur
# (and only by a tiny fraction), a Gaussian blur tends to give much nicer
# results, especially when applied to natural images.

for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)

# =========================================
# Median
# 
# Tradiationally, the median blur method has been the most effective when removing
# salt-and-pepper noise. 

# Unlike average blurring and Gaussian blurring where the kernel size could be rectangular,
# the kernel size for the median must be square.
# Futhermore (unlike the averaging method), instead of replacing the central pixel with the 
# average of the neighborhood, we instead replace the central pixel with the median of the neighborhood.

# The reason median blurring is more effective at removing salt-and-pepper style noise from an image
# is that each central pixel is always replaced with a pixel intensity that exists in the image.
# And since the median is robust to outliers, the salt-and-pepper noise will be less influential 
# to the median than another statistical method, such as the average.

# Again, methods such as averaging and Gaussian compute means or weighted means for the neighborhood 
# — this average pixel intensity may or may not be present in the neighborhood. 
# But by definition, the median pixel must exist in our neighborhood. 
# By replacing our central pixel with a median rather than an average, 
# we can substantially reduce noise.

# loop over the kernel sizes and apply a "Median" blur to the image
for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median {}".format(k), blurred)
    cv2.waitKey(0)

# =========================================
# Bilateral

# Thus far, the intention of our blurring methods have been to reduce noise and detail in an image;
# however, as a side effect we have tended to lose edges in the image.

# In order to reduce noise while still maintaining edges, we can use bilateral blurring.
# Bilateral blurring accomplishes this by introducing two Gaussian Distributions.

# The first Gaussian function only considers spatial neighbors. That is, pixels that appear close
# together in the (x,y)-coordinate space of the image.

# The second Gaussian then models the pixel intensity of the neigborhood, ensuring that only pixels with
# similar intensity are included in the actual computation of the blur.

# Intuitively, this make sense. If pixels in the same (small) neighborhood have a similar pixel value, 
# then they likely represent the same object. 

# But if two pixels in the same neighborhood have contrasting values, then we could be examining
# the edge or boundary of an object - and we would like to preserve this edge.

# Overall, this method is able to preserve edges of an image, while still reducing noise.
# The largest downside of thsi method is that it is considerably slower than its averaging, 
# Gaussian, and median blurring counterparts.


# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
    # apply bilateral filtering and display the image
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)
    cv2.waitKey(0)

# 2nd Parameter
# The diameter of our pixel neighborhood — the larger this diameter is, 
# the more pixels will be included in the blurring computation. 
# Think of this parameter as a square kernel size.

# 3rd Parameter
# Color Standard Deviation. A larger value means that more color in the neigborhood will be considered
# when computing the blur. 
# If the value get too large in respect to the diameter, then we essentially have broken the assumption of
# bilateral filtering - that only pixels of similar color should contribute significantly to the blur.

# 4th Parameter
# Space Standard Deviation. A larger value means that pixels farther out from the central pixel
# diameter iwll influence blurring calculation.

