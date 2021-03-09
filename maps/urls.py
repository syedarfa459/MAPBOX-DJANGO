from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_map, name='homemap')
]