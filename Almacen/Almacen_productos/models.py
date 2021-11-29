from django.db import models
from django.db.models.base import Model

# Create your models here.

class Cliente(models.Model):

        
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    rut_cliente = models.CharField(max_length=150, verbose_name='rut cliente', null=False, default=False)
    nombre = models.CharField(max_length=150, verbose_name='nombre')
    apellido = models.CharField(max_length=150, verbose_name='apellido')
    direccion = models.CharField(max_length=150, verbose_name='direccion')
    telefono = models.IntegerField(verbose_name='telefono')
    correo = models.EmailField(max_length=250, null=False, verbose_name='correo')


    def __str__(self):
        fila ="nombre: " + self.nombre + "apellido: " + self.apellido
        return fila