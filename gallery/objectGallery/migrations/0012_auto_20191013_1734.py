# Generated by Django 2.2.5 on 2019-10-13 15:34

import datetime
from django.db import migrations, models
import upload_validator


class Migration(migrations.Migration):

    dependencies = [
        ('objectGallery', '0011_auto_20191013_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectmodel',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 17, 34, 7, 705132)),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='image_gallery',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/', validators=[upload_validator.FileTypeValidator(allowed_types=['image/png', 'image/jpeg'])], verbose_name='Obrázky k modelu'),
        ),
    ]
