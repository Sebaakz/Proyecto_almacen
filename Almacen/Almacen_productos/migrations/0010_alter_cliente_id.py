# Generated by Django 3.2.9 on 2021-11-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almacen_productos', '0009_auto_20211129_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='rut'),
        ),
    ]
