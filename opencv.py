import cv2 as cv

img = cv.imread("dog.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("gri resim", gray)
cv.imshow("orjinal goruntu", img)

cv.imwrite("graydog.jpg", gray)

cv.waitKey(0)
cv.destroyAllWindows()