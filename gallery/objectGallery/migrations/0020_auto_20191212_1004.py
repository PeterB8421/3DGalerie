# Generated by Django 2.2.5 on 2019-12-12 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objectGallery', '0019_auto_20191211_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectmodel',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 12, 10, 4, 23, 244171)),
        ),
    ]