"""
URL configuration for droneSim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from PathCalculator.views import LocationList, LocationDetail, ObstacleList, ObstacleDetail, DroneFlightList, DroneFlightDetail, CreateDroneFlightView, CreateObstacleView
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name="index.html")),
    path('home/',TemplateView.as_view(template_name="index.html")),
    path('results/',TemplateView.as_view(template_name="index.html")),
    path('map/',TemplateView.as_view(template_name="index.html")),
    path('book/',TemplateView.as_view(template_name="index.html")),
    path('createobstaclehere/',TemplateView.as_view(template_name="index.html")),
    path('locations/', LocationList.as_view(), name='location-list'),
    path('locations/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('obstacles/', ObstacleList.as_view(), name='obstacle-list'),
    path('obstacles/<int:pk>/', ObstacleDetail.as_view(), name='obstacle-detail'),
    path('droneflights/', DroneFlightList.as_view(), name='droneflight-list'),
    path('droneflights/<int:pk>/', DroneFlightDetail.as_view(), name='droneflight-detail'),
    path('createdroneflight/', CreateDroneFlightView.as_view(), name='calculateflight'),
    path('createobstacle/', CreateObstacleView.as_view(), name='createobstacle')
]