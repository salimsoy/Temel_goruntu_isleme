import cv2 as  cv 

img = cv.imread("dog.jpg")

crop = img[100:400, 100:400]


cv.imshow("orginal", img)
cv.imshow("cropped", crop)

cv.waitKey(0)
cv.destroyAllWindows()
