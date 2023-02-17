
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from person.views import (PersonCreate, PersonDelet, PersonDetail, PersonList,
                          PersonUpdate)

urlpatterns = [
    re_path(
        'create-person/$',
        login_required(PersonCreate.as_view()), 
        name="person-create"
    ),
    path(
        'detail-person/<int:pk>/',
        login_required(PersonDetail.as_view()), 
        name="person-detail"
    ),
    path(
        'update-person/<int:pk>/',
        login_required(PersonUpdate.as_view()), 
        name="person-update"
    ),
    re_path(
        'list-person/$',
        login_required(PersonList.as_view()), 
        name="person-list"
    ),
    path(
        'delet-person/<int:pk>/',
        login_required(PersonDelet.as_view()), 
        name="person-delet"
    )
    
]