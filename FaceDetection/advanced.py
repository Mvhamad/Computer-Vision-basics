from cvzone import SerialModule, FaceDetectionModule
import cv2

cam = cv2.VideoCapture(0)
dectector = FaceDetectionModule.FaceDetector()
arduino = SerialModule.SerialObject()

while True:
    success, img = cam.read()
    img, bboxs = dectector.findFaces(img)
    if bboxs:
        arduino.sendData([0, 0, 1])
    else:
        arduino.sendData([1, 0, 0])
    cv2.imshow("Webcam", img)
    cv2.waitKey(1)