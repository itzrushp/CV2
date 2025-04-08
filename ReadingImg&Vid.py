import cv2 as cv

# img = cv.imread("IMAGE.jpg")

# if img is None:
#     print("❌ Failed to load image. Check the path or filename.")
#     exit()

# cv.imshow("Image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

#Reading Videos 

capture = cv.VideoCapture("inputvid.mp4")

#We read videos frame by frame using a while loop
while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print("❌ Failed to read video or end of video reached.")
        break

    cv.imshow("Video", frame)

    # Press 'd' to exit the loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

