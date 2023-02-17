import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  TemplateView, UpdateView)

from infringement.forms import InfringementFormCreate
from infringement.models import Infringement


class InfringementCreate(CreateView):
    model = Infringement
    form_class = InfringementFormCreate
    template_name = 'infringement/infringement_create.html'
    success_url = reverse_lazy('infringements:infringement-list')
    
    def form_valid(self, form):
        form.instance.created_at = datetime.datetime.now()
        return super().form_valid(form)



class InfringementDetail(DetailView):
    model = Infringement
    template_name = 'infringement/infringement_detail.html'
    


class InfringementList(TemplateView):
    template_name = 'infringement/infringement_list.html'
    
    def get(self, request, *args, **kwargs):
        infringement_list = Infringement.objects.all()
        context = {'infringement_list': infringement_list}
        return self.render_to_response(context)