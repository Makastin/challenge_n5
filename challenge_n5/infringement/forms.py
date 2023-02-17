from django.forms import ModelForm
from django.forms.widgets import Select, TextInput

from infringement.models import Infringement


class InfringementFormCreate(ModelForm):
    class Meta:
        model = Infringement
        fields = [
            'vehicle',
            'assigned_officer',
            'comment'
            
        ]
        widgets = {
            'vehicle': Select(attrs={'class': 'form-control', 'required': 'True'}),
            'assigned_officer': Select(attrs={'class': 'form-control', 'required': 'True'}),
            'comment': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
        }
