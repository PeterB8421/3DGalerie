# Generated by Django 2.2.5 on 2019-09-30 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objectGallery', '0005_auto_20190930_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectmodel',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 17, 7, 48, 941062)),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Popis modelu'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='tags',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Tagy modelu pro vyhledávání'),
        ),
    ]
