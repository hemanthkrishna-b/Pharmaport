# Generated by Django 3.1.2 on 2020-11-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='full_name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='Username',
            field=models.CharField(max_length=264, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=64),
        ),
    ]