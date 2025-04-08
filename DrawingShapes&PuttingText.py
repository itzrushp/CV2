import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype="uint8") #black image
cv.imshow("Blank", blank)

# 1. Paint the image a certain color
# blank[:] = 0, 255, 0  - > green image ( for full blank to go green)      # 0, 0, 255 for red 
blank[200:300, 300:400] = 0, 255, 0 # only some part of it is green from certain pixels 
cv.imshow("Green", blank) 

# 2. Draw a rectangle
# cv.rectangle(image, start_point, end_point, color, thickness)
cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=2)
cv.imshow("Rectangle", blank)

cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=cv.FILLED) #filled rectangle or can also say thickness = -1
cv.imshow("Rectangle", blank)

cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[1]//2), (0, 255, 0), thickness=2) #another way
cv.imshow("Rectangle", blank)


# 3. Draw a circle
# cv.circle(image, center_coordinates, radius, color, thickness)

cv.circle(blank, (blank.shape[1]//2 , blank.shape[0]//2), 40 , (0,0,255), thickness= -1)
cv.imshow("Circle", blank)

# 4. Draw a line
# cv.line(image, start_point, end_point, color, thickness)  

cv.line(blank, (100, 250), (blank.shape[1], blank.shape[0]), (255, 255, 255), thickness=3) 
cv.imshow("Line", blank)


# 5. Write text on image
# cv.putText(image, text, org, font, font_scale, color, thickness, lineType)

cv.putText(blank, "Hello, OpenCV!", (100, 100), cv.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255), 2)
cv.imshow("Text", blank)


cv.waitKey(0) 