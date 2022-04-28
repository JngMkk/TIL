from django.urls import path
from weather_app import views

urlpatterns = [
    path('', views.index),
    path('weather/', views.weather, name="weather"),
]