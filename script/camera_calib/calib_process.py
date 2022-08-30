#!/usr/bin/env python
from tkinter import image_names
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
cb_2d_img_points[:, :2] = np.mgrid()

# Arrays to store object points and image points from all the images
list_cb_3d_points = []  # 3d points in real world
list_cb_2d_img_points = []  # 2d points in image plane