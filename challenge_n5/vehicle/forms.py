from django.forms import ModelForm
from django.forms.widgets import EmailInput, Select, TextInput

from vehicle.models import Vehicle


class VehicleFormCreate(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'person',
            'plate',
            'brand',
            'color'
            
        ]
        widgets = {
            'person': Select(attrs={'class': 'form-control', 'required': 'True'}),
            'plate': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'brand': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'color': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            
        }



class VehicleFormUpdate(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'person',
            'plate',
            'brand',
            'color'
            
        ]
        widgets = {
            'person': Select(attrs={'class': 'form-control', 'required': 'True'}),
            'plate': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'brand': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'color': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            
        }
