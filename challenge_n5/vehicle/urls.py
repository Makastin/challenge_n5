
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from vehicle.views import (VehicleCreate, VehicleDelet, VehicleDetail,
                           VehicleList, VehicleUpdate)

urlpatterns = [
    re_path(
        'create-vehicle/$',
        login_required(VehicleCreate.as_view()), 
        name="vehicle-create"
    ),
    path(
        'detail-vehicle/<int:pk>/',
        login_required(VehicleDetail.as_view()), 
        name="vehicle-detail"
    ),
    path(
        'update-vehicle/<int:pk>/',
        login_required(VehicleUpdate.as_view()), 
        name="vehicle-update"
    ),
    re_path(
        'list-vehicle/$',
        login_required(VehicleList.as_view()), 
        name="vehicle-list"
    ),
    path(
        'delet-vehicle/<int:pk>/',
        login_required(VehicleDelet.as_view()), 
        name="vehicle-delet"
    )
    
]