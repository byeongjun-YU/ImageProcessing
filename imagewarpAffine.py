# cv2.warpAffine(image, M, dsize) : 이미지의 위치를 변경하는 함수.
# M : 변환 행렬
# dsize : Manual Size

# 단순히 이미지의 위치를 변경할 때 변환 행렬.
# [1 0 tx] tx : 가로로 이동할 거리 , ty : 세로로 이동할 거리.
# [0 1 ty] 이라는 변환 행렬이 있을 때, (a,b)의 좌표는
#          (1 * a + 0 * b + tx , 0 * a + 1 * b + ty)으로 이동.
#          변환 행렬에 [a]
#                    [b]
#                    [1] 을 곱하는 것과 같은 결과(?)

import cv2
import numpy as np

image = cv2.imread('result_ocean.png')

height, width = image.shape[:2] # 행과 열 정보만 저장.

M_move = np.float32([[1, 0, 50], [0, 1, 10]]) # 변환 행렬 생성.
result_move = cv2.warpAffine(image, M_move, (width, height))
cv2.imshow('Image Move', result_move)
cv2.waitKey(0)

# cv2.getRotationMatrix2D(center, angle, scale) : 이미지 회전을 위한 변환 행렬 생성.
# center : 회전 중심
# angle : 회전 각도
# scale : Scale Factor

# 이미지 회전의 기본 변환 행렬 , alpha = a , beta = b 라고 가정.
# [ a b (1-a)*center.x-b*center.y]
# [-b a b*center.x+(1+a)*center.y]
# a(alpha) = scale * cos(theta) , b(beta) = scale * sin(theta)

image = cv2.imread('result_ocean.png')

height, width = image.shape[:2]

M_turn = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.7) # 변환 행렬 생성.
result_turn = cv2.warpAffine(image, M_turn, (width, height))
cv2.imshow('Image Turn', result_turn)
cv2.waitKey(0)