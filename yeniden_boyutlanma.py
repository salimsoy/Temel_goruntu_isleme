import cv2 as cv 

img  = cv.imread("dog.jpg")

with_img = 200
high_img = 100
new_img = cv.resize(img, (with_img, high_img))

cv.imshow("orginal", img)
cv.imshow("resize", new_img)

cv.waitKey(0)
cv.destroyAllWindows()
