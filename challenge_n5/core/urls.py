"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.urls import include, path

from autentication.views import Home, LoginView

urlpatterns = [
    path(
        'admin/', 
        admin.site.urls
    ),
    path(
        'api/v1.0/',
        include(
            (
                'api.urls', 
                'api'
            ), 
        namespace='api'
        )
    ),
     path(
        '', 
    LoginView.as_view(),
    name='login'
    ),
    path(
        'logout/',
        logout_then_login, 
        name="logout",
    ),
    path(
        'home/', 
        login_required(Home.as_view()), 
        name="home"
    ),
    path(
        'persons/', 
        include(
            (
                'person.urls', 
                'person'
            ), 
        namespace='persons'
        )
    ),
    path(
        'officers/', 
        include(
            (
                'officer.urls', 
                'officer'
            ), 
        namespace='officers'
        )
    ),
    path(
        'vehicles/', 
        include(
            (
                'vehicle.urls', 
                'vehicle'
            ), 
        namespace='vehicles'
        )
    ),
    path(
        'infringements/', 
        include(
            (
                'infringement.urls', 
                'infringement'
            ), 
        namespace='infringements'
        )
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
