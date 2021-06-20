import numpy as np
import cv2
from numpy.core.fromnumeric import shape
from numpy.lib.histograms import histogram
from scipy.spatial.distance import seuclidean
import imutils
class ColorDescriptor:
	def devide(self,img):
		_blocks_in_row = 4
		_blocks_in_col = 4
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
			hist = self.histogram(block)
			# print('len hist:',len(hist))
			features.extend(hist)
		# extract a color histogram from the elliptical region and
		# update the feature vector
		# return the feature vector
		# print(len(features))
		return features
	def histogram(self, image):
		r,g,b = cv2.split(image)
		his = np.concatenate((self.calcHistogram(r),self.calcHistogram(g),self.calcHistogram(b)),axis=None)
		# print(his)
		return his
	def calcHistogram(selft,channel):
		bins_color = 5
		range_bin = 256/bins_color
		hist = np.zeros(bins_color)
		for i in range(channel.shape[0]):
			for j in range(channel.shape[1]):
				val = int(channel[i][j]/range_bin)
				hist[val]+=1
		# print(hist)
		cv2.normalize(hist,hist,norm_type=cv2.NORM_L2)
		# print(hist)
		return hist

if __name__ == '__main__':
	pathimg = 'static/dataset1/video1_Image0.jpg'
	img = cv2.imread(pathimg)
	cd = ColorDescriptor()
	cd.describe(img)
	# features = cd.describe(img)
	# print(len(features))
	# cv2.imshow("input",img)
	# cv2.waitKey(0)