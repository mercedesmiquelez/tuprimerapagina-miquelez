from django.db import models

# Create your models here.


class Curso(models.Model):
    
    nombre = models.CharField(max_length=100)
    numero_comision = models.IntegerField()
    
class Profesor(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    
class Entregable(models.Model):
    
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    