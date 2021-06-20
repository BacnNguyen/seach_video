from django import forms
  
class FormUpload(forms.Form):
    name = forms.CharField()
    image_field = forms.ImageField()

class FormSelect(forms.Form):
    image_query = forms.ImageField()