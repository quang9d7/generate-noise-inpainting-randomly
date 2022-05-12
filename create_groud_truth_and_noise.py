import numpy as np
import cv2 as cv

mask=cv.imread("data_paint.png")

img=cv.imread("test.png")

dst=cv.bitwise_and(img,mask)
cv.imwrite("ground_truth.png",dst)

print(mask.shape)
print(mask.dtype)