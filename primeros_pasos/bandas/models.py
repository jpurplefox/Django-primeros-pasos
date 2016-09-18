from django.db import models
from django.urls import reverse

# Create your models here.
class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.DateField()
    genero = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('banda-detail', kwargs={'pk': self.pk})
