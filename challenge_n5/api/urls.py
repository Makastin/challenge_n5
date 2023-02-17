from django.urls import path
from rest_framework.authtoken import views

from api.views import InfringementCreate, InfringementSearch

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path("infringement-create/", InfringementCreate.as_view(), name="infringement-create"),
    path("infringement-search/", InfringementSearch.as_view(), name="infringement-search")
]
