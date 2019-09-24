from django.db import models

class ObjectModel(models.Model):
    author = models.CharField(max_length=100)
    description = models.TextField()
    image_gallery = models.FileField(upload_to="uploads/")
    obj_file = models.FileField(upload_to="obj/")
    mtl_file = models.FileField(upload_to="mtl/")
    creation_date = models.DateTimeField()