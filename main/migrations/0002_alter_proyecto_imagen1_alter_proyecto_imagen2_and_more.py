# Generated by Django 4.2.5 on 2023-11-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='Proyectos'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='Proyectos'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='Proyectos'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='Logo',
            field=models.ImageField(blank=True, null=True, upload_to='Proyectos'),
        ),
    ]
