import cv2 as cv

IMG_PATH: str = "./photo.png"

image = cv.imread(IMG_PATH)
cv.imshow("Image", image)
cv.waitKey(0)

image = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)
cv.imshow("Image", image)
cv.waitKey(0)

image = cv.flip(image, 0)
cv.imshow("Image", image)
cv.waitKey(0)

image = cv.rotate(image, cv.ROTATE_90_COUNTERCLOCKWISE)
cv.imshow("Image", image)
cv.waitKey(0)

image = cv.flip(image, 1)
cv.imshow("Image", image)
cv.waitKey(0)

cv.destroyAllWindows()
