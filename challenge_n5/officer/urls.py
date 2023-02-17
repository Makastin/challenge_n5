
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from officer.views import (OfficerCreate, OfficerDelet, OfficerDetail,
                           OfficerList, OfficerUpdate)

urlpatterns = [
    re_path(
        'create-officer/$',
        login_required(OfficerCreate.as_view()), 
        name="officer-create"
    ),
    path(
        'detail-officer/<int:pk>/',
        login_required(OfficerDetail.as_view()), 
        name="officer-detail"
    ),
    path(
        'update-officer/<int:pk>/',
        login_required(OfficerUpdate.as_view()), 
        name="officer-update"
    ),
    re_path(
        'list-officer/$',
        login_required(OfficerList.as_view()), 
        name="officer-list"
    ),
    path(
        'delet-officer/<int:pk>/',
        login_required(OfficerDelet.as_view()), 
        name="officer-delet"
    )
    
]