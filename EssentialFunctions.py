import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('image.jpg')
cv.imshow("Image", img)

#1. Coverting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)
 



#2. Blur
# syntax: cv.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT) # the numbers in the bracket should be odd
cv.imshow("Blurred Image", blur)




# 3. Edge Cascade
# syntax: cv.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
# The Canny edge detector uses two thresholds to detect edges in an image.
edges = cv.Canny(blur, 125, 175)
cv.imshow("Edges when passing blur img", edges)

non_blur_edges = cv.Canny(img, 125, 175)
cv.imshow("Edges when passing img", non_blur_edges)



# 4. Dilating the image
# syntax: cv.dilate(src, kernel, anchor=None, iterations=None, borderType=None, borderValue=None)
# The dilation operation increases the white region in the image or increases the size of the foreground object.
# It is useful in closing small holes in the foreground.
dilated_canny = cv.dilate(edges, (7, 7), iterations=3) # dilate the edges 
cv.imshow("Dilated Edges", dilated_canny)


# 5. Eroding the image
# syntax: cv.erode(src, kernel, anchor=None, iterations=None, borderType=None, borderValue=None)
# The erosion operation erodes away the boundaries of the foreground object.
# It is useful in removing small white regions (noise) in the foreground.
eroded = cv.erode(dilated_canny, (7, 7), iterations=3) # erode the edges
cv.imshow("Eroded Edges", eroded)


# 6. Resizing the image
# syntax: cv.resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None) 
# The resize function is used to resize the image to a specified size.
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # resize the image to 500x500       
cv.imshow("Resized Image", resized)



# 7. Cropping the image
# syntax: img[y:y+h, x:x+w] 
# The cropping operation is used to crop the image to a specified size.
cropped = img[50:200, 200:400] # crop the image to 50x50
cv.imshow("Cropped Image", cropped)



cv.waitKey(0)