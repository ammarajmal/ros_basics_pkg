#!/usr/bin/env python3
import numpy as np
import cv2, time
cv2.namedWindow("Aruco Marker Detection")
cv2.moveWindow("Aruco Marker Detection", 0, 0)
video_capture = cv2.VideoCapture(0)

video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
video_capture.set(cv2.CAP_PROP_FPS, 40)

prev_frame_time = time.time()
cal_image_count = 0
frame_count = 0

while (True):
    ret, frame = video_capture.read()
    
    frame_count += 1
    if frame_count == 30:
        cv2.imwrite("cal_image_"+ str(cal_image_count)+ ".jpg", frame)
        cal_image_count += 1
        frame_count = 0


    new_frame_time = time.time()
    fps = 1/(new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    cv2.putText(frame, "FPS:" + str(int(fps)), (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (100, 255,0), 2, cv2.LINE_AA)
    cv2.imshow("Aruco Marker Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows() 