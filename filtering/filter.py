# 컨벌루션 계산 - 커널을 적용해 계산.

import cv2
import numpy as np

origin = cv2.imread('flowr.jpg')
cv2.imshow('Flower', origin)
cv2.waitKey(0)

# Basic Blurring

basicblur = cv2.blur(origin, (4, 4))
cv2.imshow('Basic_f', basicblur)
cv2.waitKey(0)

# Gaussian Blurring

Gaussianblur = cv2.GaussianBlur(origin, (5, 5), 0)
cv2.imshow('Gaussian_f', Gaussianblur)
cv2.waitKey(0)
