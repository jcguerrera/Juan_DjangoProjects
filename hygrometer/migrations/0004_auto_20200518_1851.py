# Generated by Django 3.0.3 on 2020-05-18 23:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hygrometer', '0003_auto_20200518_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indicador',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]