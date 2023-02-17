from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  TemplateView, UpdateView)

from officer.forms import OfficerFormCreate, OfficerFormUpdate
from officer.models import Officer


class OfficerCreate(CreateView):
    model = Officer
    form_class = OfficerFormCreate
    template_name = 'officer/officer_create.html'
    success_url = reverse_lazy('officers:officer-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class OfficerDetail(DetailView):
    model = Officer
    template_name = 'officer/officer_detail.html'
    


class OfficerUpdate(UpdateView):
    model = Officer
    form_class = OfficerFormUpdate
    template_name = 'officer/officer_update.html'
    success_url = reverse_lazy('officers:officer-list')
    
    def form_valid(self, form):
        return super().form_valid(form)



class OfficerDelet(DeleteView):
    model = Officer
    success_url = reverse_lazy('officers:officer-list')



class OfficerList(TemplateView):
    template_name = 'officer/officer_list.html'
    
    def get(self, request, *args, **kwargs):
        officer_list = Officer.objects.all()
        context = {'officer_list': officer_list}
        return self.render_to_response(context)