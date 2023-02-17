from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  TemplateView, UpdateView)

from person.forms import PersonFormCreate, PersonFormUpdate
from person.models import Person


class PersonCreate(CreateView):
    model = Person
    form_class = PersonFormCreate
    template_name = 'person/person_create.html'
    success_url = reverse_lazy('persons:person-list')
    
    def form_valid(self, form):
        return super().form_valid(form)



class PersonDetail(DetailView):
    model = Person
    template_name = 'person/person_detail.html'
    


class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonFormUpdate
    template_name = 'person/person_update.html'
    success_url = reverse_lazy('persons:person-list')
    
    def form_valid(self, form):
        return super().form_valid(form)



class PersonDelet(DeleteView):
    model = Person
    success_url = reverse_lazy('persons:person-list')



class PersonList(TemplateView):
    template_name = 'person/person_list.html'
    
    def get(self, request, *args, **kwargs):
        person_list = Person.objects.all()
        context = {'person_list': person_list}
        return self.render_to_response(context)