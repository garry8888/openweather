from django.urls import path

from . import views

urlpatterns = [
    path('', views.current_weather, name='current_weather'),
    path('hourly/', views.hourly_weather, name='hourly_weather'),
]