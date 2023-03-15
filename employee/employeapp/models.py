from django.db import models

from . import choices


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=20, choices=choices.POSITION, default='EMPLOYEE')
    manager = models.CharField(max_length=50)
    skill = models.CharField(max_length=20)
    rating= models.PositiveIntegerField()

    def __str__(self):
        return self.name
