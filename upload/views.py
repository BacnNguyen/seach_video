from django.shortcuts import render
from .form import FormUpload 
# Create your views here.
from .models import GeeksModel
import os
def upload(request):
    context = {}
    if request.method == "POST":
        form = FormUpload(request.POST, request.FILES)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            print("Name of file:",name)
            img = form.cleaned_data.get("image_field")
            path="static/images/"+str(img)
            obj = GeeksModel.objects.create(
                                title = name, 
                                img = img
                                )
            obj.save()
    return render(request, "upload/upload.html",{"form":FormUpload})