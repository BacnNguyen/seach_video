import cv2
def devide(img):
    _blocks_in_row = 6
    _blocks_in_col = 6
    img = cv2.resize(img,(600,600))
    h,w= img.shape[:2]
    # print("{}:{}".format(w,h))
    win_size_row =  int(w/_blocks_in_row)
    win_size_col = int(h/_blocks_in_col)
    win = []
    # print("block:{}-{}".format(win_size_row,win_size_col))
    for r in range(0,w,win_size_row):
        for c in range(0,h,win_size_col):
            temp = img[r:r+win_size_row,c:c+win_size_col]
            win.append(temp)
    # print(len(win))
    # for i in range(len(win)):
    #     cv2.imshow("block {}".format(i),win[i])
    return win
if __name__ =='__main__':
    img = cv2.imread("/static/images/100.png")
    devide(img)
    # cv2.waitKey(0