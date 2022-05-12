import cv2 as cv

im_color = cv.imread("test.png", cv.IMREAD_COLOR)
im_gray = cv.cvtColor(im_color, cv.COLOR_BGR2GRAY)


_, mask = cv.threshold(im_gray, thresh=180, maxval=255, type=cv.THRESH_BINARY)
im_thresh_gray = cv.bitwise_and(im_gray, mask)

mask3 = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)  # 3 channel mask

im_thresh_color = cv.bitwise_and(im_color, mask3)

cv.imshow("original image", im_color)
cv.imshow("binary mask", mask)
cv.imshow("3 channel mask", mask3)
cv.imshow("im_thresh_gray", im_thresh_gray)
cv.imshow("im_thresh_color", im_thresh_color)
cv.imwrite("binary_mask.png",mask)
cv.waitKey(0)
