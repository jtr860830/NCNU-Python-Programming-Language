import cv2 as cv
import numpy as np

IMG_PATH: str = "./photo.png"

original_image = cv.imread(IMG_PATH)
alpha: float = 0.5
beta: int = 100
image = np.uint8(np.clip((original_image * alpha + beta), 0, 255))
cv.imshow("Image", image)
cv.waitKey(0)
cv.destroyAllWindows()
