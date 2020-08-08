# Generated by Django 3.0.3 on 2020-08-08 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_auto_20200809_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='str_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main.Store'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='str_id',
            field=models.OneToOneField(default=5, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
