# cv2.add() : Saturation 연산 수행 - 0보다 작으면 0, 255보다 크면 255로 표현.
# np.add() : Modulo 연산 수행 - 다시 0부터 시작 , 255 = 255, 256 = 0, 257 = 1 이런식.
#                              255를 넘어가면 임의의 수 A / 256 의 나머지를 픽셀 값으로 가짐.
#                              np.add()는 잘 사용되지 않음.

import cv2

image_1 = cv2.imread('gradation.jpg')
image_2 = cv2.imread('unicon.jpg')

img_Add1 = cv2.add(image_1, image_2)
cv2.imshow('Image Add1', img_Add1)
cv2.waitKey(0)

img_Add2 = image_1 + image_2
cv2.imshow('Image Add2', img_Add2)
cv2.waitKey(0)