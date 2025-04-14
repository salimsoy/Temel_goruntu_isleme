import cv2 as cv 

img = cv.imread("dog.jpg")

h, w, _ = img.shape

center = (w // 2, h // 2)
angle = 90
scale = 1.0

transform_matrix = cv.getRotationMatrix2D(center, angle, scale)

rotate = cv.warpAffine(img, transform_matrix, (w, h))

cv.imshow("orginal", img)
cv.imshow("rotated", rotate)

cv.waitKey(0)
cv.destroyAllWindows()
