import cv2 as cv 

img = cv.imread("dog.jpg")
circle = img.copy()
rectangle = img.copy()
line = img.copy()

center = (70, 70)
radius = 40
color = (0, 0, 255)
thickness = 4

cv.circle(circle, center, radius, color, thickness)

start_point = (50,50)
end_point = (200,200)

cv.rectangle(rectangle, start_point, end_point, color ,thickness)

pt1 = (300, 300)
pt2 = (350, 400)

cv.line(line, pt1, pt2, color, thickness)

cv.imshow("orginal", img)
cv.imshow("daire", circle)
cv.imshow("dikdörtgen", rectangle)
cv.imshow("cizgi", line)

cv.waitKey(0)
cv.destroyAllWindows()