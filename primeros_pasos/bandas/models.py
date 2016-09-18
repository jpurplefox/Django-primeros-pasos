from django.db import models

# Create your models here.
class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.DateField()
    genero = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
