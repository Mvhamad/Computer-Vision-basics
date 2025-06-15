import cv2
from cvzone import SerialModule, FaceDetectionModule 

cam = cv2.VideoCapture(0)
dectector = FaceDetectionModule.FaceDetector(0.3)
arduino = SerialModule.SerialObject()

while True:
    success, img = cam.read()
    img, bboxs = dectector.findFaces(img)
    if bboxs:
        arduino.sendData([1])
    else:
        arduino.sendData([0])
    cv2.imshow("Webcam", img)
    cv2.waitKey(1)

# Description:
# This code captures video from the webcam, detects faces using the cvzone FaceDetector, and sends data to an Arduino via serial communication.
# If a face is detected, it sends a signal (1) to the Arduino; if no face is detected, it sends a different signal (0).