from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [

    path('', views.home_map, name='homemap'),
    path('favicon\.ico', RedirectView.as_view(url='/static/images/favicon.ico'))
]
