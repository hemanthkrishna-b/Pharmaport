# Generated by Django 2.2.16 on 2020-12-12 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0003_auto_20201212_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 12, 12, 59, 45, 708108)),
        ),
    ]
