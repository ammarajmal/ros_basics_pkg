#!/usr/bin/env python
import numpy as np
import cv2 as cv
import glob

cb_width = 8
cb_height = 6
cb_square_size = 26.22

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points
cb_3D_points = np.zeros((cb_width * cb_height, 3), np.float32)
cb_3D_points[:, :2] = np.mgrid[0:cb_width, 0:cb_height].T.reshape(-1, 2) * cb_square_size

# Arrays to store object points and image points from all the images
list_cb_3d_points = []  # 3d points in real world
list_cb_2d_img_points = []  # 2d points in image plane

list_images = glob.glob('*.jpg')

for frame_name in list_images:
    img = cv.imread(frame_name)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chessboard corners
    ret, corners = cv.findChessboardCorners(gray, (cb_width, cb_height), None)
    # if found, add object points, image points (after refining them)
    if ret is True:
        list_cb_3d_points.append(cb_3D_points)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        list_cb_2d_img_points.append(corners2)
        # Draw adn display the corners
        cv.drawChessboardCorners(img, (cb_width, cb_height), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
cv.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(list_cb_3d_points, list_cb_2d_img_points, gray.shape[::-1], None, None)
print('Calibration Matrix: ')
print(mtx)
print('Distortion: ', dist)

with open('camera_calib.npy', 'wb') as f:
    np.save(f, mtx)
    np.save(f, dist)
