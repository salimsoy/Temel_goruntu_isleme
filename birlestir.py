import cv2 as cv 

img = cv.imread("dog.jpg")
img1 = cv.imread("graydog.jpg")

combineh = cv.hconcat([img, img1])
combinev = cv.vconcat([img, img1])

cv.imshow("horizontal combine", combineh)
cv.imshow("vertical combine", combinev)

cv.waitKey(0)
cv.destroyAllWindows()


