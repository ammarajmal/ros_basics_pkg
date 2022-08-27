#!/usr/bin/env python3

# *****************
# example 1
# *****************
# import cv2 as cv
# import numpy as np
# img = cv.imread('my_image.jpg')
# cv.imshow('imaage',img)
# cv.imwrite('new_image.png', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # *************************************************
# # example 1: Open BGR and MatplotLib RGB Coloring
# # *************************************************
# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
# img = cv.imread('my_image.jpg')

# # b,g,r = cv.split(img);  img2 = cv.merge([r, g, b])
# img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# # img2 = img[:,:,::-1]

# plt.subplot(121); plt.imshow(img)
# plt.subplot(122); plt.imshow(img2)
# plt.show()
# cv.imshow('bgr image', img)
# cv.imshow('rgb image', img2)
# cv.waitKey(0) & 0XFF 
# cv.destroyAllWindows()


# *************************************
# Example 2: Basic Operations on Images
# *************************************
import cv2 as cv
import numpy as np
img = cv.imread('my_image2.tif')

# Accessing and Modifying pixel values
px = img[10, 10];    print(px)

# accessing only the blue pixel value

blue = img[10, 10, 0];   print(blue)


# printing the size of the image
print(img.size)


# cv.imshow('bgr image', img)
# cv.waitKey(0) & 0XFF 
# cv.destroyAllWindows()




# *****************
# example last (webcam video stream)
# *****************

# cap = cv2.VideoCapture(0)

# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         cv2.imshow('Frame', frame)
#         if cv2.waitKey(25) & 0xFF == ord('q'):  break
#     else:   break
# cap.release()
# cv2.destroyAllWindows()
    
# Load a color image in grayscale