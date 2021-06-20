import cv2
import os
from . import ccv_extract
from . import csv_file
import numpy as np

def mysort(e):
    return e[1]
def distance(listA,listB):
    # print(type(imageA))
    dis = 0
    # print(len(listB))
    for i in range(len(listA)):
        dis+= (np.abs(listA[i][0]-listB[i][0])+np.abs(listA[i][1]-listB[i][1]))
    return dis
def process(query_img_path,db_path):
    q_img = cv2.imread(query_img_path)
    # cv2.imshow("Query Image",q_img)
    # vec_f = ccv_extract.extract_color_feature(q_img)
    vec_f = ccv_extract.extract_color_feature_bgr(q_img)
    # print(vec_f)
    name_video,name_image,vector_feature = csv_file.read(db_path)
    # print(len(vector_feature))
    # print(type(vec_f))
    # print(type(vector_feature[0]))
    # min_dis = 500000
    list_dis = []
    # idx = -1
    for i in range(len(vector_feature)):
    # for i in range(5):
        dis = distance(vec_f,vector_feature[i])
        list_dis.append((i,dis))
        # print("Distance:",dis)
        # if dis<min_dis:
        #     min_dis = dis
        #     idx = i
    # print("Min dis:",min_dis)
    list_dis.sort(key= mysort)
    res_path_video =[]
    for i in range(10):
        temp = name_video[list_dis[i][0]]+".mp4"
        if temp not in res_path_video:
            print("{}-{}".format(temp,list_dis[i][1]))
            res_path_video.append(temp)
            if len(res_path_video)==5:
                break
    # best_result = name_video[idx]+".mp4"
    # res_path_image = name_image[idx]+".jpg"
    # return res_path_video,res_path_image
    return res_path_video
    # res_path = "G:\\Ky2_Nam4\\CSDLDaPhuongTien\\feature_images\\"+name_video[idx]+"\\"+name_image[idx]
    # print("Most similar video:{} : images {} : distance= {}".format(name_video[idx],name_image[idx],min_dis))
    # img = cv2.imread(res_path)
    # cv2.imshow("Result",img)
    # cv2.waitKey(0)
if __name__ =='__main__':
    # img_query_path = "G:\\Ky2_Nam4\\CSDLDaPhuongTien\\query_image\\q2.jpg"
    img_query_path = "G:\\Ky2_Nam4\\CSDLDaPhuongTien\\query_image\\video (3)\\Image1.jpg"
    db_path ="feature3000.csv"
    process(img_query_path,db_path)
    # lis1 = [-7,-4]
    # lis2 = [17,6.5]
    # print(euclid_distance(lis1,lis2))
    # lis = [(8475, 1407), (0, 1304), (0, 160), (0, 170), (43995, 722), (11444, 1665), (0, 2386), (0, 715), (0, 389), (0, 249), (0, 245), (0, 83), (0, 128), (0, 288), (14825, 1350)]
    # print(lis[0][1])