import cv2
import numpy as np

img = cv2.imread('number.png')
kernel1 = np.ones((5, 5), np.uint8)
erode1 = cv2.erode(img, kernel1, iterations=1)
dilate1 = cv2.dilate(img, kernel1, iterations=1)

cv2.imshow('origin_number', img)
cv2.waitKey(0)
cv2.imshow('erode_number', erode1)
cv2.waitKey(0)
cv2.imshow('dilate_number', dilate1)
cv2.waitKey(0)

img_morphol = cv2.imread('morphol.png')
kernel2 = np.ones((7, 7), np.uint8)

erode2 = cv2.erode(img_morphol, kernel2, iterations=1)
dilate2 = cv2.dilate(img_morphol, kernel2, iterations=1)
opening = cv2.morphologyEx(img_morphol, cv2.MORPH_OPEN, kernel2)
closing = cv2.morphologyEx(img_morphol, cv2.MORPH_CLOSE, kernel2)

cv2.imshow('erode_morphol', erode2)
cv2.waitKey(0)
cv2.imshow('dilate_morphol', dilate2)
cv2.waitKey(0)
cv2.imshow('opening_morphol', opening)
cv2.waitKey(0)
cv2.imshow('closing_morphol', closing)
cv2.waitKey(0)