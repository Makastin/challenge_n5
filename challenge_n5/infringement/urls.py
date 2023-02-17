
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from infringement.views import (InfringementCreate, InfringementDetail,
                                InfringementList)

urlpatterns = [
    re_path(
        'create-infringement/$',
        login_required(InfringementCreate.as_view()), 
        name="infringement-create"
    ),
    path(
        'detail-infringement/<int:pk>/',
        login_required(InfringementDetail.as_view()), 
        name="infringement-detail"
    ),
    re_path(
        'list-infringement/$',
        login_required(InfringementList.as_view()), 
        name="infringement-list"
    )
    
]