from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .validators import *

class ModelForm(forms.Form):
    author = forms.CharField(required=True, label="Autor modelu")
    name = forms.CharField(required=True, label="Název modelu")
    description = forms.TextInput(attrs={'size': 10, 'required': False, 'title':"Popis modelu"})
    img_gallery = forms.ImageField(required=False, label="Obrázky k modelu")
    obj_file = forms.FileField(required=True, label="OBJ soubor modelu")
    mtl_file = forms.FileField(required=True, label="MTL soubor modelu")
    create_date = forms.DateTimeField(default=datetime.now())
    tags = forms.CharField(required=False, label="Tagy modelu")

    def clean_author(self):
        data = self.cleaned_data['author']

        if len(data) > 100:
            raise ValidationError(_("Maximální délka je 100 znaků."))
        else:
            return data

    def clean_name(self):
        data = self.cleaned_data['name']

        if len(data) > 500:
            raise ValidationError(_("Maximální délka je 500 znaků."))
        else:
            return data

    def clean_img_gallery(self):
        data = self.cleaned_data['img_gallery']

        if validate_img_extension(data):
            return data

    def clean_obj_file(self):
        data = self.cleaned_data['obj_file']

        if validate_obj_extension(data):
            return data

    def clean_mtl_file(self):
        data = self.cleaned_data['mtl_file']

        if validate_mtl_extension(data):
            return data

    