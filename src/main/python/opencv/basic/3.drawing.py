import numpy as np
import cv2

# 3 Most basic methods to draw shapes
# - Line: cv2.line. cv2.line(arr, p1, p2, color). p1=(cX,cY), color=(b,g,r)
# - Rectangle: cv2.rectangle
# - Circle = cv2.circle

# Draw Line
canvas = np.zeros((300,300,3), dtype=np.uint8) 
# canvas = np.zeros((300,300,3), dtype="uint8")
green = (0, 255, 0)
cv2.line(canvas, (0,0), (300,300), green)
display(Image.fromarray(canvas))

# Draw Rectangle
p1 = (10,10)
p2 = (60,60)
red = (0, 0, 255)
thickness = 3 # -1 = filled rectangle
cv2.rectangle(canvas, p1, p2, red, thickness)

# Draw random circles
for i in range(0, 25):
    # randomly generate a radius size between 5 and 200, generate a random
    # color, and then pick a random point on our canvas where the circle
    # will be drawn
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size = (3,)).tolist()
    pt = np.random.randint(0, high=300, size = (2,))

    # draw our random circle
    cv2.circle(canvas, tuple(pt), radius, color, -1)

