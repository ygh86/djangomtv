from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} - {self.parentesco} - {self.fecha_nacimiento}"