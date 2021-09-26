from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime

# Create your models here.
class UserManager(models.Manager):

    def basic_validator(self, postData):
        today = date.today()
        errores = {}
        if len(postData['title']) < 3:
            errores['title'] = "Debe ingresar un título de al menos 3 letras"
        if len(postData['network']) < 4:
            errores['network'] = "Debe ingresar un network de al menos 4 letras"
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errores['description'] = 'La descripción debe estar vacía o tener al mínimo 10 letras'
        if postData['r_date'] > str(today):
            errores['r_date'] = 'La fecha de lanzamiento debe ser menor a la fecha actual'
        return errores


class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()