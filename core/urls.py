from django.urls import path
from . import views

urlpatterns = [
    path('api/locations/<str:city>/<int:days>/', views.weather_forecast, name="weather_forecast"),
]

