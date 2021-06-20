# import the necessary packages
import cv2
import numpy as np
import csv
from scipy.spatial.distance import euclidean
from search.csvfile import read
from search.colordescriptor import ColorDescriptor
class Searcher:
	def __init__(self, indexPath):
		# store our index path
		self.indexPath = indexPath
    
	def search(self, queryFeatures, limit = 5):
		# initialize our dictionary of results
		results = {}
        # open the index file for reading
		name_video,name_image,features = read(self.indexPath)
		for i in range(len(features)):
			d = euclidean(features[i],queryFeatures)
			name = "{}//{}".format(name_video[i],name_image[i])
			results[name] = d
		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results = sorted([(v, k) for (k, v) in results.items()])
		# return our (limited) results
		return results[:limit]
	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
		# return the chi-squared distance
		return d
if __name__=='__main__':
	pathimg = 'static/dataset1/video1_Image0.jpg'
	csv_path = "G:\\Ky2_Nam4\\CSDLDaPhuongTien\\search-image-main\\search-image-main\\static\\color_hist.csv"
	img = cv2.imread(pathimg)
	cd = ColorDescriptor()
	q_fea = cd.describe(img)
	s = Searcher(csv_path)
	result = s.search(q_fea)
	print(len(result))
	print(result[0][1])