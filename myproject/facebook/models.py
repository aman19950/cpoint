from pyexpat import model
from django.db import models


# Create your models here.


class register_info(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
