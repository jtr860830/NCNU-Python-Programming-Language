import cv2 as cv

IMG_PATH: str = "./photo.png"

original_image = cv.imread(IMG_PATH)
gray_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
cv.imshow("Image", gray_image)
cv.waitKey(0)
cv.destroyAllWindows()
