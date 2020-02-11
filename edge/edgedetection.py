# Canny Edge Detector
# cv2.Canny(image, threshold1, threshold2) : 엣지를 검출하는 함수
# image : 입력 이미지
# threshold1 : 최소 스레숄드 값 , threshold2 : 최대 스레숄드 값

import cv2

image_gray = cv2.imread('iu.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("IU", image_gray)
cv2.waitKey(0)

image_canny = cv2.Canny(image_gray, 50, 150)
cv2.imshow("Canny IU", image_canny)
cv2.waitKey(0)

def nothing():
    pass
img_gray = cv2.imread('iu.jpg', cv2.IMREAD_GRAYSCALE)


cv2.namedWindow("Canny Edge")
cv2.createTrackbar('low thresh', 'Canny Edge', 0, 1000, nothing)
cv2.createTrackbar('high thresh', 'Canny Edge', 0, 1000, nothing)

cv2.setTrackbarPos('low thresh', 'Canny Edge', 50)
cv2.setTrackbarPos('high thresh', 'Canny Edge', 150)

cv2.imshow("IU2", img_gray)

while True:

    low = cv2.getTrackbarPos('low thresh', 'Canny Edge')
    high = cv2.getTrackbarPos('high thresh', 'Canny Edge')

    img_canny = cv2.Canny(img_gray, low, high)
    cv2.imshow("Canny Edge", img_canny)

    if cv2.waitKey(1)&0xFF == 27:
        break