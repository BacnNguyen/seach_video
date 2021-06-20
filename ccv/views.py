from django.http.response import HttpResponse
from django.shortcuts import render
from numpy.core.fromnumeric import ptp
from .form import FormSelect
import cv2
from .colordescriptor import ColorDescriptor
from .searcher import Searcher
import pathlib
import os
from upload.models import GeeksModel
from .csv_file import read
from .ccv_extract import extract_color_feature
from .searchVideo import process
import time
# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        form = FormSelect(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get("image_query")
            
            
            obj = GeeksModel.objects.create( 
                                title ="{}-{}".format(str(int(time.time())),str(img)),
                                img = img
                                )
            obj.save()
            query_path=obj.getPath()
            print(query_path)
            # print(GeeksModel.objects.filter(img= path)!='')
            # if GeeksModel.objects.filter(img= path)=='':
            #     q=GeeksModel.objects.get(img= path)
            # else:
            #     obj = GeeksModel.objects.create(
            #                         title = name, 
            #                         img = img
            #                         )
            #     obj.save()
            context['filename']=query_path.split("/")[-1]
            db_path = "static/feature3000bgr.csv"
            #CCV process
            res_video= process(query_path,db_path)
            context['url']= res_video
            # context['result_video'] = best_result
            # print(len(res_video))
            # print(res_video)
            # cd = ColorDescriptor((8, 8, 8))
            # query = cv2.imread(query_path)
            # # print(query)
            # features = cd.describe(query)
            # # print(features)
            # searcher = Searcher("static/index1.csv")
            # results = searcher.search(features)
            # # display the query
            # print(results)
            # urlImage=[]
            # # loop over the result
            # for (score, resultID) in results:
            #     # load the result image and display it
            #     name_image = resultID.split("\\")[-1]
            #     name_video = name_image.split("_")[0]
            #     # print(name_video)
            #     print(name_image)
            #     urlImage.append(name_image)
            #     context['url']=urlImage
              
    else:
        form = FormSelect()
    context['form']= FormSelect
    
    
    return render(request, "ccv/index.html", context)