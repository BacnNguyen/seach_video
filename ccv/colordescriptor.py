import numpy as np
import cv2
import imutils
class ColorDescriptor:
	def __init__(self, bins):
		# store the number of bins for the 3D histogram
		self.bins = bins

	def devide(self,img):
		_blocks_in_row = 3
		_blocks_in_col = 3
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
	def describe(self, image):
		# convert the image to the HSV color space and initialize
		# the features used to quantify the image
		# image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		blocks=self.devide(image)
		# print(len(blocks))
		features = []
		# grab the dimensions and compute the center of the image
		for block in blocks:			
			hist = self.histogram(block,None)
			features.extend(hist)
		# extract a color histogram from the elliptical region and
		# update the feature vector
		# return the feature vector
		return features
	def histogram(self, image, mask):
    # extract a 3D color histogram from the masked region of the
    # image, using the supplied number of bins per channel
		hist = cv2.calcHist(images=[image], channels=[0, 1, 2], mask=None,
                            histSize=self.bins, ranges=[0, 256] * 3)
		# normalize the histogram if we are using OpenCV 2.4
		if imutils.is_cv2():
			hist = cv2.normalize(hist).flatten()
		# otherwise handle for OpenCV 3+
		else:
			hist = cv2.normalize(hist, hist).flatten()
		# return the histogram
		return hist
if __name__ =='__main__':
	pathimg = 'static/dataset1/video1_Image0.jpg'
	img = cv2.imread(pathimg)
	bins = (8,8,8)
	hist = cv2.calcHist(images=img, channels=[0,1,2], mask=None,
                            histSize=(8,8,8), ranges=[0, 256]*3)
	print('shape:',hist.shape)
	print(len(hist))
	cd = ColorDescriptor((8, 8, 8))
	features = cd.describe(img)
	print(len(features))
	# cv2.imshow("input",img)
	# cv2.waitKey(0)