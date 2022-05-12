import cv2 as cv
import os,sys


path_A="ground_truth"
path_B="noise_data"

src_path="data"

dir_A=os.listdir(path_A)
dir_B=os.listdir(path_B)

n=len(dir_A)
print(n)

for i in range(0,n):
    file_A=dir_A[i]
    file_B=dir_B[i]
    path_file_A=os.path.join(path_A,file_A)    
    path_file_B=os.path.join(path_B,file_B)

    img_A=cv.imread(path_file_A)
    img_B=cv.imread(path_file_B)
    
    concat_img=cv.hconcat([img_B,img_A])

    file_name=file_A[0:file_A.find(".")]+ "_concat"+".png"

    cv.imwrite(os.path.join(src_path,file_name),concat_img)