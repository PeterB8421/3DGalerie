from django.db import models
from datetime import datetime
from upload_validator import FileTypeValidator
from django.conf import settings
import os

class ObjectModel(models.Model):
    author = models.CharField("Autor modelu", max_length=100)
    name = models.CharField("Název 3D modelu", max_length=500)
    description = models.TextField("Popis modelu", null=True, blank=True, default=None)
    obj_file = models.FileField("OBJ soubor 3D modelu", upload_to="obj/")
    mtl_file = models.FileField("MTL soubor 3D modelu", upload_to="mtl/", null=True, blank=True, default=None)
    creation_date = models.DateTimeField(default=datetime.now())
    tags = models.CharField("Tagy modelu pro vyhledávání", max_length=1000, null=True, blank=True, default=None)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.obj_file.name))
        if self.mtl_file != "":
            os.remove(os.path.join(settings.MEDIA_ROOT, self.mtl_file.name))
        super(ObjectModel, self).delete(*args, **kwargs)


class Files(models.Model):
    model_id = models.ForeignKey(ObjectModel, on_delete=models.CASCADE, blank=True, default=None)
    f = models.FileField("Soubor k modelu",default=None ,blank=True,null=True,upload_to="images/", 
    validators=[FileTypeValidator(allowed_types=["image/jpeg", "image/png", "image/bmp"], allowed_extensions=[".jpg", ".jpeg", ".png", ".bmp"])])

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.f.name))
        super(Files, self).delete(*args, **kwargs)