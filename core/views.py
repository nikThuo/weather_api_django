from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

import requests
from datetime import datetime
from statistics import mean, median

# Create your views here.
'''
Function to consume Open Weather API and compute maximum, minimum,
average and median temperature of a city for given number of days.
The days range from 1-6.
'''

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def weather_forecast(request, city, days):
    api_key = '522d93ca74535f59f74f954375677536'


    api_url = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}'
    lat = requests.get(api_url).json()[0]['lat']
    lon = requests.get(api_url).json()[0]['lon']

    forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
    res = requests.get(forecast_url).json()
    list = res['list']

    now = str(datetime.now()).split(' ')[0]

    temperatures = []
    for item in list:
        if now == item['dt_txt'].split()[0]:
            temp = item['main']['temp']
            temperatures.append(temp)
            now_temp = now.split('-')
            now = f'{now_temp[0]}-{now_temp[1]}-{int(now_temp[2])+1}'

    if days in range(1,7):
        min_temp = temperatures[:days]
        temp_dict = {
            'maximum': max(min_temp),
            'minimum': min(min_temp),
            'average': mean(min_temp),
            'median': median(min_temp)
        }

        return Response(temp_dict, 200)
    else:
        return Response({'error': 'Day out of range. Input has to be between 1-6.'}, 400)



