from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento = models.DateTimeField()
    parentesco = models.CharField(max_length=30)

    def __str__(self):
        return f'Nombre :{self.nombre} Edad: {self.edad}  Parentesco: {self.parentesco}'