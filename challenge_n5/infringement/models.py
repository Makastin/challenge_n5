import uuid

from django.db import models

from officer.models import Officer
from vehicle.models import Vehicle


class Infringement(models.Model):
    vehicle = models.ForeignKey(
        Vehicle, 
        on_delete=models.CASCADE,
        verbose_name='Vehicle'
    )
    created_at = models.DateTimeField(
        auto_now=False,
        verbose_name='Created at',
        editable=True 
    )
    assigned_officer = models.ForeignKey(
        Officer, 
        on_delete=models.CASCADE,
        verbose_name='Assigned Officer'
    )
    infringement_id = models.UUIDField(
        default=uuid.uuid4, 
        editable=False,
        verbose_name='Infringment ID'
    )
    comment = models.TextField(
        verbose_name='Comment about infringement',
        blank=True,
        null=True
    )
    
    

    class Meta:
     
        verbose_name = 'Infringement'
        verbose_name_plural = 'Infringements'

    
    def __str__(self):
            return str(self.infringement_id)