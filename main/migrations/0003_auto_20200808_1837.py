# Generated by Django 3.0.3 on 2020-08-08 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200808_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='st_loc_longitude',
            new_name='str_loc_longitude',
        ),
    ]
