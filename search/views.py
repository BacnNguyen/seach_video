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
            # print(GeeksModel.objects.filter(img= path)!='')
            # if GeeksModel.objects.filter(img= path)=='':
            #     q=GeeksModel.objects.get(img= path)
            # else:
            #     obj = GeeksModel.objects.create(
            #                         title = name, 
            #                         img = img
            #                         )
            #     obj.save()
            # print(query_path)
            context['filename']=query_path.split("/")[-1]
            cd = ColorDescriptor()
            query = cv2.imread(query_path)
            # print(query)
            features = cd.describe(query)
            # print(features)
            searcher = Searcher("static/color_hist_16blocks.csv")
            results = searcher.search(features)
            # display the query
            # print(results)
            urlImage=[]
            # loop over the result
            res =[]
            for (d, name) in results:
                name_video = name.split('//')[0]
                if name_video+".mp4" in res:
                    continue
                res.append(name_video+".mp4")
            context['url']=res
              
    else:
        form = FormSelect()
    context['form']= FormSelect
    
    
    return render(request, "search/index.html", context)