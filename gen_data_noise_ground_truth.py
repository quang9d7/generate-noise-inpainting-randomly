import os,sys
import cv2 as cv
import numpy as np

src_path="ground_truth"
dst_path="noise_data"
dirs=os.listdir(src_path)

h,w=512,512
isClosed = False
color = (0, 0, 0)
thickness = 20
x_coordiration=w//2
y_coordiration=h//2-50
central_point=(x_coordiration,y_coordiration)
radius=120

x_upper=x_coordiration+radius
x_lower=x_coordiration-radius
y_upper=y_coordiration+radius
y_lower=y_coordiration-radius
isClosed = False

for file in dirs:
    file_name=file[0:file.find(".")]+".png"
    print(file_name)
    path_file=os.path.join(src_path,file)
    img=cv.imread(path_file)
    inter =np.random.randint(6,10)
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

    cv.imwrite(os.path.join(dst_path,file_name),img)