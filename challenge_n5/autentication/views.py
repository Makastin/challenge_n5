 ## Django packages ##
## MODEL BANK AND CREDITS APP ##
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from infringement.models import Infringement
from officer.models import Officer
from person.models import Person
from vehicle.models import Vehicle


## Login View ##
class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login/login.html'
    success_url = success_url = reverse_lazy('home')


## Home View ##
class Home(TemplateView):
    template_name = "home/home.html"
    
    def get(self, request, *args, **kwargs):
        persons = Person.objects.count()
        officers = Officer.objects.count()
        vehicles = Vehicle.objects.select_related('person').count()
        infringements = Infringement.objects.select_related('person', 'assigned_officer').count()
        
        context = {
            'persons': persons,
            'officers':officers,
            'vehicles':vehicles,
            'infringements':infringements
        }
        return self.render_to_response(context)
