from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  TemplateView, UpdateView)

from vehicle.forms import VehicleFormCreate, VehicleFormUpdate
from vehicle.models import Vehicle


class VehicleCreate(CreateView):
    model = Vehicle
    form_class = VehicleFormCreate
    template_name = 'vehicle/vehicle_create.html'
    success_url = reverse_lazy('vehicles:vehicle-list')
    
    def form_valid(self, form):
        return super().form_valid(form)



class VehicleDetail(DetailView):
    model = Vehicle
    template_name = 'vehicle/vehicle_detail.html'
    


class VehicleUpdate(UpdateView):
    model = Vehicle
    form_class = VehicleFormUpdate
    template_name = 'vehicle/vehicle_update.html'
    success_url = reverse_lazy('vehicles:vehicle-list')
    
    def form_valid(self, form):
        return super().form_valid(form)



class VehicleDelet(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicles:vehicle-list')



class VehicleList(TemplateView):
    template_name = 'vehicle/vehicle_list.html'
    
    def get(self, request, *args, **kwargs):
        vehicle_list = Vehicle.objects.all()
        context = {'vehicle_list': vehicle_list}
        return self.render_to_response(context)