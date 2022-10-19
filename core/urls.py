from django.urls import path
from . import views

urlpatterns = [
    # path('locations/<str:pk>/', views.delete, name="delete"),
    # path('api/locations/(?P<city>[^/]+)$/(?P<days>[^/]+)$/', views.weather_forecast, name="weather_forecast"),
    path('api/locations/<str:city>/<int:days>/', views.weather_forecast, name="weather_forecast"),
]

# /api/locations/{city}/?days={number_of_days}