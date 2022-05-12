import cv2 as cv
import numpy as np

binary_mask=cv.imread("binary_mask.png")
painted_mask=cv.imread("data_paint.png")
cv.imshow("painted mask",painted_mask)




binary_mask=binary_mask/255
cv.imshow("binary mask after diving 255",binary_mask)
np_zero=np.count_nonzero(binary_mask==1)
print(np_zero)
join_mask=binary_mask*painted_mask
cv.imshow("join_mask",join_mask)
cv.imwrite("join_mask.png",join_mask)
cv.waitKey(0)