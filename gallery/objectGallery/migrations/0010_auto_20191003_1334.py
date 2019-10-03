# Generated by Django 2.2.5 on 2019-10-03 11:34

import datetime
from django.db import migrations, models
import upload_validator


class Migration(migrations.Migration):

    dependencies = [
        ('objectGallery', '0009_auto_20191002_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectmodel',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 3, 13, 34, 26, 812989)),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='image_gallery',
            field=models.FileField(blank=True, default=None, null=True, upload_to='uploads/', validators=[upload_validator.FileTypeValidator(allowed_types=['image/png', 'image/jpeg'])], verbose_name='Obrázky k modelu'),
        ),
    ]
