#!/usr/bin/env python
import numpy as np
import cv2
import time
import cv2.aruco as aruco

marker_size = 100

with open('camera_calib.npy', 'rb') as f:
    camera_matrix = np.load(f)
    camera_distortion = np.load(f)

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)

cv2.namedWindow('Image Feed')
cv2.moveWindow('Image Feed', 159, 0)


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 40)

prev_frame_time = time.time()

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to grayscale

    # Find all the aruco markers in the image
    corners, ids, rejected = aruco.detectMarkers(gray_frame, aruco_dict, camera_matrix, camera_distortion)
    print(ids)
    
    if ids is not None:
        aruco.drawDetectedMarkers(frame, corners)  # draw a box around all the detected markers
        # get pose of all single markers
        rvec, tvec, _objPoints = aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, camera_distortion)
        # draw axis and write ids on all markers
        for marker in range(len(ids)):
            aruco.drawAxis(frame, camera_matrix, camera_distortion, rvec[marker], tvec[marker], 100)
            cv2.putText(frame, str(ids[marker][0]), (int(corners[marker][0][0][0]) - 30, int(corners[marker][0][0][0])), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2, cv2.LINE_AA)

    new_frame_time = time.time()
    fps = 1/(new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    cv2.putText(frame,
                "FPS:" + str(int(fps)), 
                (10, 40),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (100, 255, 0),
                2,
                cv2.LINE_AA)
    cv2.imshow("Image Feed", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
