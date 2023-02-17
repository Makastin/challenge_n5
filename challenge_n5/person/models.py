from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length = 150,
        verbose_name='Full Name'
    )
    
    email = models.EmailField(
        max_length=254,
        verbose_name='person Email',
        unique=True
    )    

    class Meta:
    
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return self.name
