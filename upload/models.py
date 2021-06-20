from django.db import models

# Create your models here.
from django.db import models
import time
# Create your models here.


def directory_path(instance, filename):
    return "static/images/"+str(int(time.time()))+filename
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = directory_path)
  
    def __str__(self):
        return self.title
    def getPath(self):
        path= "G:\\Ky2_Nam4\\CSDLDaPhuongTien\\search-image-main\\search-image-main\\static\\images\\"
        return str(self.img)