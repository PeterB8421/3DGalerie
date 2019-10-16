from django.db import models
from datetime import datetime
from upload_validator import FileTypeValidator
from django.conf import settings

class ObjectModel(models.Model):
    author = models.CharField("Autor modelu", max_length=100)
    name = models.CharField("Název 3D modelu", max_length=500)
    description = models.TextField("Popis modelu", null=True, blank=True, default=None)
    image_gallery = models.ImageField("Obrázky k modelu", blank=True, null=True, default=None, upload_to="uploads/", validators=[FileTypeValidator(
        allowed_types=["image/png", "image/jpeg"])])
    obj_file = models.FileField("OBJ soubor 3D modelu", upload_to="obj/")
    mtl_file = models.FileField("MTL soubor 3D modelu", upload_to="mtl/")
    creation_date = models.DateTimeField(default=datetime.now())
    tags = models.CharField("Tagy modelu pro vyhledávání", max_length=1000, null=True, blank=True, default=None)