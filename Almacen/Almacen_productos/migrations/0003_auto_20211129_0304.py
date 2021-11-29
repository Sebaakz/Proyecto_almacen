# Generated by Django 3.2.9 on 2021-11-29 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almacen_productos', '0002_auto_20211129_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='existecia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_existencia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='familia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_familia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_marca', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='productos',
            name='exist_actual',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='marca',
        ),
    ]
