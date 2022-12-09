from django.db import models
from django.core import validators
# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, blank =False, unique=True)
    description = models.CharField(unique=False, blank=True, max_length=120)
    quantity = models.IntegerField(unique = False, validators = [ 
        validators.MaxValueValidator(100),
        validators.MinValueValidator(0),

    ])
