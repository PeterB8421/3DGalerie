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


    