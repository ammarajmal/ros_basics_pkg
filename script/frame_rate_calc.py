#!/usr/bin/env python
import numpy as np
import cv2 as cv
import time

cv.namedWindow('Image Feed')
cv.moveWindow('Image Feed', 159, 0)


cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv.CAP_PROP_FPS, 40)

prev_frame_time = time.time()

while True:
    ret, frame = cap.read()
    new_frame_time = time.time()
    fps = 1/(new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    cv.putText(frame,
                "FPS:" + str(int(fps)), 
                (10, 40),
                cv.FONT_HERSHEY_PLAIN,
                2,
                (100, 255, 0),
                2,
                cv.LINE_AA)
    cv.imshow("Image Feed", frame)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
