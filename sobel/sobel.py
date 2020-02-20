import cv2
import numpy as np

img = cv2.imread('b.png')

cv2.imshow('Origin', img)
cv2.waitKey(0)

sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)

sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)

sobelxy = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize=3)
cv2.imshow('Sobel XY', sobelxy)
cv2.waitKey(0)
