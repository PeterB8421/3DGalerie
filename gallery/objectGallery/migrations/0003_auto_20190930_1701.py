# Generated by Django 2.2.5 on 2019-09-30 15:01

import datetime
from django.db import migrations, models
import objectGallery.validators


class Migration(migrations.Migration):

    dependencies = [
        ('objectGallery', '0002_auto_20190930_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectmodel',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 17, 1, 6, 497733)),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='image_gallery',
            field=models.FileField(blank=True, upload_to='uploads/', validators=[objectGallery.validators.validate_img_extension], verbose_name='Obrázky k modelu'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='mtl_file',
            field=models.FileField(upload_to='mtl/', validators=[objectGallery.validators.validate_mtl_extension], verbose_name='MTL soubor 3D modelu'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='obj_file',
            field=models.FileField(upload_to='obj/', validators=[objectGallery.validators.validate_obj_extension], verbose_name='OBJ soubor 3D modelu'),
        ),
    ]
