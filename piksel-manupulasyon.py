import cv2 as cv

img = cv.imread("dog.jpg")
img1 = cv.imread("dog.jpg", 0)

gray = cv.cvtColor(img1, cv.COLOR_GRAY2BGR)

pixel_gray = gray[150:250, 150:250]

img[150:250, 150:250] = pixel_gray

cv.imshow("orginal", img)
cv.imshow("gray", gray)

cv.waitKey(0)
cv.destroyAllWindows()
