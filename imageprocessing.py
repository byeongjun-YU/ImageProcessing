# cv2.imread(file_name, flag) : 이미지를 읽어 Numpy 객체로 만드는 함수.
# file_name : 읽고자 하는 이미지 파일.
# flag : 이미지를 읽는 방법 설정.
# IMREAD_COLOR : 이미지를 Color로 읽고, 투명한 부분은 무시.
# IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽기.
# IMREAD_UNCHANGED : 이미지를 Color로 읽고, 투명한 부분도 읽기.
# cv2.imshow(title, image) : 특정한 이미지를 화면에 출력하는 함수.
# cv2.imwrite(file_name, image) : 특정한 파일을 이미지로 저장하는 함수.
# cv2.waitKey(time) : 키보드 입력을 처리하는 함수
import numpy as np
import cv2
import time

# 이미지 파일 읽어오기.

img_ocean = cv2.imread('ocean.jpg', cv2.IMREAD_COLOR) # 이미지 읽어오기.
cv2.imshow('Image Basic', img_ocean) # 이미지 화면에 출력.
cv2.waitKey(0) # 출력화면이 꺼지지 않도록.
cv2.imwrite('result_ocean.png', img_ocean) # 읽어온 이미지 파일로 저장.

# 이미지 파일 grayscale로 변경.
# cvtColor : 이전에 읽어들인 이미지의 특성을 바꾸는 함수.

img_gray = cv2.cvtColor(img_ocean, cv2.COLOR_BGR2GRAY) # 읽어온 파일 grayscale로 변경.
cv2.imshow('Image Gray', img_gray) # 흑백 화면 출력.
cv2.waitKey(0)
cv2.imwrite('ocean_gray.png', img_gray)

# 이미지 크기 및 픽셀 확인

Image = cv2.imread('result_ocean.png')

print(Image.shape)
print(Image.size)
px = Image[300, 300]
print(px)

# 특정 픽셀 색상 변경

Image = cv2.imread('result_ocean.png')
Image[0:130, 0:130] = [0, 0, 0]
cv2.imshow('Image White', Image)
cv2.waitKey(0)


# 특정 색상 제거

image = cv2.imread('ocean.jpg')
image[:, :, 1] = 0
cv2.imshow('Image', image)
cv2.waitKey(0)

# 특정 픽셀 복사 붙여넣기

roi_ocean = cv2.imread('ocean.jpg')
logo = roi_ocean[200:400, 250:450]
cv2.imshow('Image ROI', logo)
cv2.waitKey(0)

roi_ocean[100:300, 100:300] = logo
cv2.imshow('Image ROI', roi_ocean)
cv2.waitKey(0)