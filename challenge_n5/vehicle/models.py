from django.db import models

from person.models import Person


class Vehicle(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='Person'
    )
    
    plate = models.CharField(
        max_length = 150,
        verbose_name='Plate',
        unique=True
    )
    
    brand = models.CharField(
        max_length = 150,
        verbose_name='Brand'
    )
    
    color = models.CharField(
        max_length = 150,
        verbose_name='Color'
    )
    
    
    class Meta:
    
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return self.plate
