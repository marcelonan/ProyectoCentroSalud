from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class clases(models.Model):
    nombre = models.CharField(max_length=50)
    publico = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} - {self.publico}'

class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True, blank=True)
