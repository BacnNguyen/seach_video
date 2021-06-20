import csv
import glob
import os
import cv2
from search.colordescriptor import ColorDescriptor
# from colordescriptor import ColorDescriptor
def read(path):
    name_video = []
    name_image = []
    vector_feature = []
    # print(path)
    with open(path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if len(row)>0:
                # print(row[2])
                # print(len(row[2].split(":"))) 
                # print(row[2].split(":")) 
                # print("=========================")  
                name_video.append(row[0])
                name_image.append(row[1])
                temp = row[2][1:len(row[2])-1].split(",")
                # print(len(temp))
                # print("Feature:")
                # print(fea)
                fea = []
                for t in temp:
                    fea.append(float(t))
                vector_feature.append(fea)
    # print(len(vector_feature))
    # print(type(vector_feature))
    return name_video,name_image, vector_feature
def write(path,name_video,name_img,content):
    with open(path,mode="a") as csv_file:
        fieldnames = ['name_video','name_img','vector_feature']
        writer = csv.DictWriter(csv_file,fieldnames = fieldnames) 
        # writer.writeheader()
        # s = ""
        # for i in range(len(content)):
        #     for j in range(len(content[i])-1):
        #         s+=str(content[i][j])+","
        #     s+=str(content[i][len(content[i])-1])
        #     s+=":"
        writer.writerow({'name_video':name_video ,'name_img':name_img,'vector_feature':content})

if __name__ == '__main__':
    csv_path = "G:\\Ky2_Nam4\\CSDLDaPhuongTien\\search-image-main\\search-image-main\\static\\color_hist_16blocks.csv"
    root_path = "G:\\Ky2_Nam4\\CSDLDaPhuongTien\\image_scene\\"
    path_video = glob.glob(root_path+"*")
    video_names = []
    image_names =[]
    cd = ColorDescriptor()
    for p in path_video:
        video_name = p.split('\\')[-1]
        path_image = glob.glob(p+"\\*")
        video_names.append(video_name)
        for p_img in path_image:
            print(p_img)
            image_name = p_img.split("\\")[-1]
            image_names.append(image_name)
            img = cv2.imread(p_img)
            feature = cd.describe(img)
            write(csv_path,video_name,image_name,feature)
    
    
    
    # name_video,name_image,feature = read(csv_path)
    # print(len(feature))
    # print(len(name_video))
    # print(len(name_image))