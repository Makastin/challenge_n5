from django.forms import ModelForm
from django.forms.widgets import EmailInput, TextInput

from person.models import Person


class PersonFormCreate(ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'email',
            
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'email': EmailInput(attrs={'class': 'form-control', 'required': 'True'}),
            
        }



class PersonFormUpdate(ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'email',
            
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'email': EmailInput(attrs={'class': 'form-control', 'required': 'True'}),
            
        }


