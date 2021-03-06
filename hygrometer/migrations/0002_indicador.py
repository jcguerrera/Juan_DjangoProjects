# Generated by Django 3.0.3 on 2020-05-18 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hygrometer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(verbose_name='codigo')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('tipoIndicador', models.CharField(max_length=20, verbose_name='TipoIndicador')),
                ('prioridad', models.IntegerField(verbose_name='Prioridad')),
            ],
        ),
    ]
