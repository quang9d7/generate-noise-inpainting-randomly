import cv2 as cv
import numpy as np

img=cv.imread("test.png")
dimensions=img.shape
h,w=dimensions[0],dimensions[1]
print(f'h={h} w={w}')

area=h*w
lower_area=0.25*area
upper_area=0.5*area

# color=(255,0,0)
color=(0,0,0)
thickness=-1

pi=3.14
sum_area=0
rand_area=np.random.randint(lower_area,upper_area)
print(rand_area)

rand_area=np.random.randint(lower_area,upper_area)

while sum_area<rand_area:
    radius=np.random.randint(20,50)
    center_coordinates=(np.random.randint(0,h),np.random.randint(0,w))
    img=cv.circle(img,center_coordinates,radius,color,thickness)
    sum_area+=(pi*(radius**2))
    print(sum_area)

cv.imshow("image",img)
cv.waitKey(0)
