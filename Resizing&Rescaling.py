import cv2 as cv

# Function to resize the frame (works for Images , Videos and Webcams)
def rescaleFrame(frame, scale=0.75): #resized by 75%
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame , dimensions, interpolation=cv.INTER_AREA)

#Function to change the Resolution of the video (Works only with Live videos (webcam))
def changeRes(width, height):
    capture.set(3, width) #width
    capture.set(4, height) #height


# Load the image
img = cv.imread("IMAGE.jpg")
cv.imshow('image', img)

# Resize the image
resized_img = rescaleFrame(img, scale=0.2) #resized by 20%
cv.imshow("Image", resized_img)



#Reading Videos
capture = cv.VideoCapture("inputvid.mp4")

#We read videos frame by frame using a while loop
while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print("❌ Failed to read video or end of video reached.")
        break

    # Resize the frame
    frame_resized = rescaleFrame(frame)


    # Display the original and resized frames
    cv.imshow("Video", frame)
    cv.imshow("Resized Video", frame_resized)

    # Press 'd' to exit the loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

