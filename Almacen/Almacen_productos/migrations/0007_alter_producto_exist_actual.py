# Generated by Django 3.2.9 on 2021-11-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almacen_productos', '0006_auto_20211129_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='exist_actual',
            field=models.CharField(choices=[('Sobre Stock', 'Sobre Stock'), ('en Stock', 'en Stock'), ('bajo Stock', 'bajo Stock'), ('sin stock', 'sin stock'), ('descontinuado', 'descontinuado')], max_length=50, verbose_name='existencia'),
        ),
    ]
