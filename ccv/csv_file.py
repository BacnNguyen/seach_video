import csv
import glob
import os
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
                temp = row[2][0:len(row[2])-1].split(":")
                # print(len(temp))
                # print("Feature:")
                # print(fea)
                fea = []
                for t in temp:
                    numbers = t.split(",")
                    fea.append((int(numbers[0]),int(numbers[1])))
                vector_feature.append(fea)
    # print(len(vector_feature))
    # print(type(vector_feature))
    return name_video,name_image, vector_feature
def write(path,name_video,name_img,content):
    with open(path,mode="a") as csv_file:
        fieldnames = ['name_video','name_img','vector_feature']
        writer = csv.DictWriter(csv_file,fieldnames = fieldnames) 
        # writer.writeheader()
        s = ""
        for i in range(len(content)):
            for j in range(len(content[i])-1):
                s+=str(content[i][j])+","
            s+=str(content[i][len(content[i])-1])
            s+=":"
        writer.writerow({'name_video':name_video ,'name_img':name_img,'vector_feature':s})

if __name__ == '__main__':
    # lis = [(1,2),(3,4),(5,1)]
    # s = ""
    # for i in range(len(lis)-1):
    #     s+=str(lis[i])+"/"
    # s+=str(lis[len(lis)-1])
    # print(s)
    # st = ","
    # string = st.join(str(e) for e in lis)
    # print(type(string))
    # write("feature.csv","img.jpg", st.join(lis))
    video,image,feature = read("feature.csv")
    print(video[0])
    print(image[0])
    print(feature[0])
    print(type(feature[0][0]))
    # print(type(name))
    # print(feature[0])
    # for i in range(len(feature[0])):
    #     feature[0][i] = int(feature[0][i])
    #     print(type(feature[0][i]))
    # print(feature[0][0]+feature[0][1])
    # print(len(image))
    # print(feature[1])
    # print(feature[1][0])
    # feas = feature.split("/")
    # print(feas[0])