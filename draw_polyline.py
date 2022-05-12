from cmath import pi
import cv2 as cv
import numpy as np
#generate noise

img=cv.imread("ground_truth.png")
# img=img/255

dimension=img.shape
h,w=dimension[0],dimension[1]

num_zero=np.count_nonzero(img==0)
num_one=np.count_nonzero(img==1)

total_pixel=h*w
# print(f'probability of zero is {num_zero/total_pixel}')
# print(f'probability of one is {num_one/total_pixel}')

# print((num_zero+num_one)-total_pixel)

start_point=(0,90)
end_point=(200,90)

color=(0,255,0)
thickness=1

#img=cv.line(img,start_point,end_point,color,thickness)
x_coordiration=w//2
y_coordiration=h//2-50
central_point=(x_coordiration,y_coordiration)
radius=120

x_upper=x_coordiration+radius
x_lower=x_coordiration-radius
y_upper=y_coordiration+radius
y_lower=y_coordiration-radius
isClosed = False
color = (0, 0, 0)
thickness = 20

inter =np.random.randint(5,8)
for i in range(0,inter+1):
    x=np.random.randint(x_lower,x_upper)
    y=np.random.randint(y_lower,y_upper)

    [x_2,y_2]=[x+np.random.randint(0,20),y+np.random.randint(0,20)]
    [x_3,y_3]=[x_2+np.random.randint(0,10),y_2+np.random.randint(0,10)]
    [x_4,y_4]=[x_3+np.random.randint(0,10),y_3+np.random.randint(0,10)]
    [x_5,y_5]=[x_4+np.random.randint(0,10),y_4+np.random.randint(0,10)]
    [x_6,y_6]=[x_5+np.random.randint(0,10),y_5+np.random.randint(0,10)]
    [x_7,y_7]=[x_6+np.random.randint(0,10),y_6+np.random.randint(0,10)]

    pts = np.array([[x,y],[x_2,y_2],[x_3,y_3],[x_4,y_4],[x_5,y_5],[x_6,y_6],[x_7,y_7]]
               ,np.int32)
    pts = pts.reshape((-1, 1, 2))
  
    img = cv.polylines(img, [pts], 
                      isClosed, color, thickness)
#img=cv.circle(img,central_point,radius,color,thickness)

cv.imshow("binary mask",img)
cv.waitKey(0)