# Generated by Django 2.2.5 on 2019-10-13 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objectGallery', '0010_auto_20191003_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectmodel',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 16, 49, 47, 457138)),
        ),
    ]
