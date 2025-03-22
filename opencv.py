import cv2 as cv

img = cv.imread("dog.jpg")

cv.imshow("orjinal goruntu", img)

cv.waitKey(0)
cv.destroyAllWindows()