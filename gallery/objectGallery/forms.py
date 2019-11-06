from django import forms
from objectGallery.models import ObjectModel, Files
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .validators import *

class ObjectModelForm(forms.ModelForm):
    class Meta:
        model = ObjectModel
        fields = ["author", "name", "description", "obj_file", "mtl_file", "tags", "image_gallery"]

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

class FilesModelForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ["f"]
    