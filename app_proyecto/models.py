from django.db import models

class Cliente(models.Model):
    empresa = models.CharField(max_length=40)
    mail = models.EmailField()
    fecha_compra = models.DateField()

class Vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()
    antiguedad = models.IntegerField()

class Productos(models.Model):
    producto = models.CharField(max_length=40)
    stock = models.IntegerField()
