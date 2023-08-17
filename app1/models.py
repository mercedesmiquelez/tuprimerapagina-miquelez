from django.db import models

# Create your models here.
class Comprador(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()



class Vendedor(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=15)



class Producto(models.Model):
    nombre = models.CharField(max_length=15)
    entregado = models.BooleanField()