# Generated by Django 3.2.9 on 2021-11-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almacen_productos', '0013_auto_20211129_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]