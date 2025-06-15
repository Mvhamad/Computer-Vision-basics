from cvzone.SerialModule import SerialObject
import cv2
import numpy as np

arduino = SerialObject("COM3", 9600)
# imgPotentiometer = cv2.imread("Resources/potentiometer.jpg")

while True:
    data = arduino.getData()
    print(data)