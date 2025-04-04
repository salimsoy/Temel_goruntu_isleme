import cv2 as cv 

img = cv.imread("dog.jpg")

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

img_grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


cv.imshow("orginal", img)
cv.imshow("rgb", img_rgb)
cv.imshow("hsv", img_hsv)
cv.imshow("gray", img_grayscale)

cv.waitKey(0)
cv.destroyAllWindows()
