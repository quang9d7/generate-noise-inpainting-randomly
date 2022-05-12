import os,sys
import cv2 as cv

src_path="original_textures"
dst_path="ground_truth"
dirs=os.listdir(src_path)

mask =cv.imread("images_generate/data_paint.png")
cv.imshow("mask",mask)
cv.waitKey(0)
for file in dirs:
    # print(file)\
    file_name=file[0:file.find(".")]+".png"
    print(file_name)
    path_file=os.path.join(src_path,file)
    img=cv.imread(path_file)
    dst=cv.bitwise_and(img,mask)
    cv.imwrite(os.path.join(dst_path,file_name),dst)