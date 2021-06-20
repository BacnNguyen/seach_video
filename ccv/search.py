# import the necessary packages
from .colordescriptor import ColorDescriptor
from .searcher import Searcher
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
# initialize the image descriptor
cd = ColorDescriptor((8, 8, 8))
query = cv2.imread(args["query"])
features = cd.describe(query)
# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
# display the query
cv2.imshow("Query", query)
print(results)
print(args['result_path'])
# loop over the results
for (score, resultID) in results:
	# load the result image and display it
    name_video = resultID.split("\\")[-1]
    print(name_video)
    print(args["result_path"] + "/" + resultID)
    result = cv2.imread(args["result_path"] + "/" + name_video)
    cv2.imshow("Result", result)
    cv2.waitKey(0)