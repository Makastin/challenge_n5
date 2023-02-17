from django.forms import ModelForm
from django.forms.widgets import TextInput

from officer.models import Officer


## CLIENT CREATEFORM ##
class OfficerFormCreate(ModelForm):
    class Meta:
        model = Officer
        fields = [
            'officer_name',
            'officer_number',
            
        ]
        widgets = {
            'officer_name': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'officer_number': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            
        }


## CLIENT UPDATEFORM ##
class OfficerFormUpdate(ModelForm):
    class Meta:
        model = Officer
        fields = [
            'officer_name',
            'officer_number',
            
        ]
        widgets = {
            'officer_name': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'officer_number': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            
        }

