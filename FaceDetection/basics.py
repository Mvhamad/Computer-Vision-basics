import cv2
from cvzone.FaceDetectionModule import FaceDetector


cam = cv2.VideoCapture(0)
dectector = FaceDetector()
while True:
    success, img = cam.read()
    img, bboxs = dectector.findFaces(img)
    cv2.imshow("Webcam", img)
    cv2.waitKey(1)

# Description:
# This code captures video from the webcam, detects faces using the cvzone FaceDetector, and displays the video feed with detected faces highlighted.
# It continuously reads frames from the webcam, processes them to find faces, and shows the result in a window named "Webcam".
# The loop runs indefinitely until the user closes the window or interrupts the program.
