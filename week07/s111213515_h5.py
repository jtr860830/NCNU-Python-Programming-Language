import cv2 as cv

IMG_PATH: str = "./photo.png"
SCALE = 0.55

image = cv.imread(IMG_PATH)
height = int(image.shape[0] * SCALE)
width = int(image.shape[1] * SCALE)
resized_image = cv.resize(image, (width, height), interpolation=cv.INTER_AREA)

cv.imshow("Image", image)
cv.imshow("Resized Image", resized_image)
cv.waitKey(0)
cv.destroyAllWindows()
