# Generated by Django 2.2.16 on 2020-12-10 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_page', '0010_auto_20201210_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='metadata',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='connection_api',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 10, 18, 34, 1, 711869)),
        ),
        migrations.AlterField(
            model_name='connections_existed',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 10, 18, 34, 1, 713825)),
        ),
    ]