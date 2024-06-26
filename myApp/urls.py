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
from views import LocationList, LocationDetail, ObstacleList, ObstacleDetail, DroneFlightList, DroneFlightDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/', LocationList.as_view(), name='location-list'),
    path('locations/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('obstacles/', ObstacleList.as_view(), name='obstacle-list'),
    path('obstacles/<int:pk>/', ObstacleDetail.as_view(), name='obstacle-detail'),
    path('droneflights/', DroneFlightList.as_view(), name='droneflight-list'),
    path('droneflights/<int:pk>/', DroneFlightDetail.as_view(), name='droneflight-detail'),
]