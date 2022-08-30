#!/usr/bin/env python
# import numpy as np
# import cv2
# import cv2.aruco as aruco

# marker_size = 100

# with open('camera_calib.npy', 'rb') as f:
#     camera_matrix = np.load(f)
#     camera_distortion = np.load(f)

# aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)

# cap = cv2.VideoCapture(0)

# camera_width = 640
# camera_height = 480
# camera_frame_rate = 40

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)
# cap.set(cv2.CAP_PROP_FPS, camera_frame_rate)


# ret, frame = cap.read()  # grab a frame

# gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to grayscale

# # Find all the aruco markers in the image
# corners, ids, rejected = aruco.detectMarkers(gray_frame, aruco_dict, camera_matrix, camera_distortion)

# if ids is not None:
#     aruco.drawDetectorMarkers(frame, corners)  # draw a box around all the detected markers
#     # get pose of all single markers
#     rvec, tvec, _objPoints = aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, camera_distortion)
#     # draw axis and write ids on all markers
#     for marker in range(len(ids)):
#         aruco.drawAxis(frame, camera_matrix, camera_distortion, rvec[marker], tvec[marker], 100)
#         # cv2.putText(frame, str(ids[marker][0]), (int(corners[marker][0][0][0]) - 30, int(corners[marker][0][0][1])), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2, cv2.LINE_AA)
# cv2.imshow('frame', frame)
# cv2.waitKey(0)
# cap.release()
# cv2.destroyAllWindows()


# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import sys
