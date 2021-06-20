import cv2
import numpy as np
import glob

from numpy.lib.function_base import disp
# n=10
def print_res(result):
    for i in range(n):
        for j in range(n):
            print("{} ".format(result[i][j]),end='')
        print(end='\n')

def check1(mask,x,y,checked):
    h,w = mask.shape[:2]
    recent_val = mask[x][y]
    temp = []
    if x-1>=0 and checked[x-1][y]== False and mask[x-1][y] == recent_val :
        temp.append((x-1,y))
    if y-1 >=0 and checked[x][y-1]== False and mask[x][y-1] == recent_val:
        temp.append((x,y-1))
    if  x+1<w and checked[x+1][y]== False and mask[x+1][y] == recent_val:
        temp.append((x+1,y))
    if y+1 <h and checked[x][y+1]== False and mask[x][y+1] == recent_val:
        temp.append((x,y+1))
    if x-1>=0 and y-1>=0 and checked[x-1][y-1]== False and mask[x-1][y-1] == recent_val:
        temp.append((x-1,y-1))
    if x+1<w and y+1<h and checked[x+1][y+1]== False and mask[x+1][y+1] == recent_val: 
        temp.append((x+1,y+1))
    if x+1<w and y-1>=0 and checked[x+1][y-1]== False and mask[x+1][y-1] == recent_val: 
        temp.append((x+1,y-1))
    if x-1>=0 and y+1<h and checked[x-1][y+1]== False and mask[x-1][y+1] == recent_val: 
        temp.append((x-1,y+1))
    # print(temp)
    return temp
def check(mask,x,y,value,checked,result):
    checked[x][y] = True
    result[x][y] = value
    # print_res(result)
    recent_val = mask[x][y]
    # print("{}:{}={}".format(x,y,value))
    h,w = mask.shape[:2]
    if x-1 >=0 and checked[x-1][y]!=True:
        if mask[x-1][y] == recent_val:
            checked[x-1][y] = True
            result[x-1][y] = value
            check(mask,x-1,y,value,checked,result)
    if y-1 >=0 and checked[x][y-1]!=True:
        if mask[x][y-1] == recent_val:
            checked[x][y-1] = True
            result[x][y-1] = value
            check(mask,x,y-1,value,checked,result)
    if x+1 <w and checked[x+1][y]!=True:
        if mask[x+1][y] == recent_val:
            checked[x+1][y] = True
            result[x+1][y] = value
            check(mask,x+1,y,value,checked,result)
    if y+1 <h and checked[x][y+1]!=True:
        if mask[x][y+1] == recent_val:
            checked[x][y+1] = True
            result[x][y+1] = value
            check(mask,x,y+1,value,checked,result)
    if x+1 <w and y+1 <h and checked[x+1][y+1]!=True:
        if mask[x+1][y+1] == recent_val:
            checked[x+1][y+1] = True
            result[x+1][y+1] = value
            check(mask,x+1,y+1,value,checked,result)
    if x-1>=0 and y+1<h and checked[x-1][y+1]!=True:
        if mask[x-1][y+1] == recent_val:
            checked[x-1][y+1] = True
            result[x-1][y+1] = value
            check(mask,x-1,y+1,value,checked,result)
    if x+1 < h and y-1>=0 and checked[x+1][y-1]!=True:
        if mask[x+1][y-1] == recent_val:
            checked[x+1][y-1] = True
            result[x+1][y-1] = value
            check(mask,x+1,y-1,value,checked,result)
    if x-1>=0 and y-1>=0 and checked[x-1][y-1]!=True:
        if mask[x-1][y-1] == recent_val:
            checked[x-1][y-1] = True
            result[x-1][y-1] = value
            check(mask,x-1,y-1,value,checked,result)

def segment(test):
    checked = np.ndarray(test.shape,dtype=bool)
    result = np.ndarray(test.shape,dtype=int)
    list_color_value = []
    for i in range(test.shape[0]):
        for j in range(test.shape[1]):
            # test[i][j] = a[i][j]
            # test[i][j] = np.random.randint(0,3)
            checked[i][j] = False
            result[i][j] = -1
    # print(test)
    # print("======================================")
    value = 0
    for i in range(test.shape[0]):
        for j in range(test.shape[1]):
            if checked[i][j] == False:
                checked[i][j] = True
                list_xy = []
                list_xy.append((i,j))
                temp = check1(test,i,j,checked)
                if len(temp)== 0:
                    list_color_value.append((test[i][j],value))
                    result[i][j] = value
                    value+=1
                else:
                    list_color_value.append((test[i][j],value))
                    for e in temp:
                        list_xy.append(e)
                        checked[e[0]][e[1]] = True
                    idx = 0
                    while idx<len(list_xy):
                        # print(len(list_xy))
                        # print(list_xy)
                        temp1 = check1(test,list_xy[idx][0],list_xy[idx][1],checked)
                        idx+=1
                        for e in temp1:
                            list_xy.append(e)
                            checked[e[0]][e[1]] = True
                    for xy in list_xy:
                        result[xy[0]][xy[1]] = value
                    value+=1
    return result,value,list_color_value
def extract_ccv(gray,name):
    # cv2.imshow("GRAY",gray)
    max_range = 255
    if 'h' in name:
        max_range= 180
    bins = 5
    w_bin = max_range/bins #width of bins
    tau = 3000
    mask = np.ndarray(gray.shape,dtype=int)
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            idx = int(gray[i][j]/w_bin)
            if idx == bins:
                idx -=1
            mask[i][j] = idx
    result,max_val,list_color_value = segment(mask)
    # print(list_color_value)
    statis_value = []
    for i in range(max_val):
        statis_value.append(0)
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            statis_value[result[i][j]]+=1
    # print(statis_value)

    statis_color_coherence = [0]*bins
    statis_color_incoherence = [0]*bins
    for i in list_color_value:
        color_bin = i[0]
        label = i[1]
        if statis_value[label]>tau:
            statis_color_coherence[color_bin]+=statis_value[label]
        else:
            statis_color_incoherence[color_bin]+=statis_value[label]
    # print(statis_color)
    result_vector = []
    for i in range(len(statis_color_coherence)):
        result_vector.append((statis_color_coherence[i],statis_color_incoherence[i]))
    return result_vector
    # coherence = []
    # for i in range(len(statis_color)):
    #     if statis_color[i] >0:
    #         coherence.append((i,statis_color[i]))

    # print_res(result)
    # for i in range(30):
    #     for j in range(30):
    #         print("{} ".format(mask[i][j]),end='')
    #     print(end='\n')

    # count = 0
    # for i in range(len(statis_value)):
    #     if statis_value[i] >5*tau:
    #         count +=1
    # print("count =",count)
    # w_color = int(255/count)
    # new_colors = []
    # level = 1
    # for i in range(len(statis_value)):
    #     if statis_value[i] >5*tau:
    #         new_colors.append(level*w_color)
    #         level+=1
    #     else:
    #         new_colors.append(0)   
    
    # segment_image = np.ndarray(mask.shape,dtype=int)
    # for i in range(gray.shape[0]):
    #     for j in range(gray.shape[1]):
    #         segment_image[i][j] = new_colors[result[i][j]]
    # segment_image = segment_image.astype(np.uint8)
    # cv2.imshow("Segment_image:"+name,segment_image)

    # print(segment_image)
def extract_color_feature(img):
    img= cv2.resize(img,(300,300))
    img = cv2.blur(img,(3,3))
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    vector_feature = extract_ccv(h,"h")+extract_ccv(s,"s")+extract_ccv(v,"v")   
    # vector_feature = extract_ccv(h,"h")+extract_ccv(s,"s")   
    # vector_feature = extract_ccv(h,"h")
    return vector_feature

def extract_color_feature_bgr(img):
    img= cv2.resize(img,(300,300))
    img = cv2.blur(img,(3,3))
    b,g,r = cv2.split(img)
    # vector_feature = extract_ccv(h,"h")+extract_ccv(s,"s")+extract_ccv(v,"v")   
    # vector_feature = extract_ccv(h,"h")+extract_ccv(s,"s")   
    vector_feature = extract_ccv(b,"b")+extract_ccv(g,"g")+extract_ccv(r,"r")
    return vector_feature
def L1distance(v,v1):
    dis = 0
    for i in range(len(v)):
        dis+=(np.abs(v[i][0]-v1[i][0])+np.abs(v[i][1]-v1[i][1]))
    return dis
def myFunc(e):
    return e[1]
if __name__ == '__main__':
    img = cv2.imread("G:\\Ky2_Nam4\\CSDLDaPhuongTien\\feature_images\\video (2)\\Image1.jpg")
    img1 = cv2.imread("G:\\Ky2_Nam4\\CSDLDaPhuongTien\\query_image\\video (51)\\Image3.jpg")
    # images = glob.glob("I:\\AI\\Opencv\\CompareImages\\CompareImages\\images\\*.jpg")
    # img1 = cv2.imread("img3.jpg")
    v= extract_color_feature(img)
    v1= extract_color_feature(img1)
    print(v)
    print("======================")
    print(v1)
    print("========================")
    print(L1distance(v,v1))
    # dis = []
    # for i in images:
    #     name = i.split("\\")[-1]
    #     img_i = cv2.imread(i)
    #     v_i = extract_color_feature(img_i)
    #     d = L1distance(v1,v_i)
    #     dis.append((name,d))
    
    # dis.sort(key=myFunc)
    # for d in dis:
    #     print(d)
    # # dis = L1distance(v,v1)
    # print(dis)
    # print(extract_color_feature(img1))
    # cv2.imshow("IMG",img)
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # test = np.ndarray((n,n),dtype=int)
    # checked = np.ndarray((n,n),dtype=bool)
    # result = np.ndarray((n,n),dtype=int)
    #TEST======================
    # a =     [[1 ,1, 1 ,2, 1], 
    #         [1, 2, 2 ,0, 0] ,
    #         [1 ,2 ,2, 0 ,1] ,
    #         [1, 1, 1 ,1, 0], 
    #         [0, 0 ,0, 2 ,0]]
    # test = np.ndarray((n,n),dtype=int)
    # for i in range(n):
    #     for j in range(n):
    #         # test[i][j] = a[i][j]
    #         test[i][j] = np.random.randint(0,3)
    #         # checked[i][j] = False
    #         # result[i][j] = 0
    # res = segment(test)
    # print_res(res)