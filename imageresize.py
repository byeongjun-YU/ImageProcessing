# cv2.resize(image, dsize, fx, fy, interpolation) : 이미지의 크기를 변형하는 함수.
# dsize : Manual Size
# fx : 가로 비율 , fy : 세로 비율
# interpolation - 1. INTER_CUBIC : 사이즈를 크게 할 때 사용.
#                 2. INTER_AREA : 사이즈를 작게 할 때 사용.

import cv2

img_resized = cv2.imread('result_ocean.png')
cv2.imshow('Image', img_resized)
cv2.waitKey(0)

img_expand = cv2.resize(img_resized, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Image Expand', img_expand)
cv2.waitKey(0)

img_reduce = cv2.resize(img_resized, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
cv2.imshow('Image Reduce', img_reduce)
cv2.waitKey(0)
