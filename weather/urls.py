from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='weather update'),
    path('city', views.city, name='city weather update'),
]
