# Generated by Django 2.2.5 on 2019-09-30 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objectGallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectmodel',
            name='tags',
            field=models.CharField(default='', max_length=1000, verbose_name='Tagy modelu pro vyhledávání'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Autor modelu'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 16, 49, 32, 539162)),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='description',
            field=models.TextField(blank=True, verbose_name='Popis modelu'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='image_gallery',
            field=models.FileField(blank=True, upload_to='uploads/', verbose_name='Obrázky k modelu'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='mtl_file',
            field=models.FileField(upload_to='mtl/', verbose_name='MTL soubor 3D modelu'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='obj_file',
            field=models.FileField(upload_to='obj/', verbose_name='OBJ soubor 3D modelu'),
        ),
    ]