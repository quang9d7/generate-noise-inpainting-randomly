import cv2 
import numpy as np

image=cv2.imread("test.png")
# creating a mask of that has the same dimensions of the image
# where each pixel is valued at 0
mask = np.zeros(image.shape[:2], dtype="uint8")
 
# creating a rectangle on the mask
# where the pixels are valued at 255
cv2.circle(mask, (250, 250), 200, 255, -1)
cv2.imshow("Mask", mask)
 
# performing a bitwise_and with the image and the mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to Image", masked)
print(type (masked))
gray_mask=cv2.cvtColor(masked,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray mask",gray_mask)
im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, mask_binary = cv2.threshold(im_gray, thresh=180, maxval=255, type=cv2.THRESH_BINARY)

(thresh, im_bw) = cv2.threshold(gray_mask, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("binary mask circle", im_bw)
cv2.imshow("binary mask", mask_binary)
print(type (mask_binary))
cv2.waitKey(0)

cv2.imwrite("data.png",im_bw)