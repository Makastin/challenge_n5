from django.contrib.auth.models import User
from django.db import models


class Officer(models.Model):
    officer_name = models.CharField(
        max_length = 150,
        verbose_name='Officer Name'
    )
    officer_number = models.BigIntegerField(
        verbose_name='Officer Plate Number',
        unique=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
        blank=True,
        null=True
    )
    
    
    class Meta:
    
        verbose_name = 'Officer'
        verbose_name_plural = 'Officers'

    def __str__(self):
        return self.officer_name