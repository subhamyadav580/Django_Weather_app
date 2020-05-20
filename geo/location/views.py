from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime

# Create your views here.


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=0b1adf0e4f723b8e847168e41784d6be'
    if request.method == 'POST':
        city = request.POST['location']
        r = requests.get(url.format(city)).json()
        sunrise = datetime.fromtimestamp(r['sys']['sunrise'])
        sunset = datetime.fromtimestamp(r['sys']['sunset'])
        dt = datetime.fromtimestamp(r['dt'])
        weather_data = {
            'city': city,
            'temperature': r['main']['temp'],
            'temp_min': r['main']['temp_min'],
            'temp_max': r['main']['temp_max'],
            'description': r['weather'][0]['description'],
            'wind': r['wind']['speed'],
            'country': r['sys']['country'],
            'humidity': r['main']['humidity'],
            'icon': r['weather'][0]['icon'],
            'date': dt,
            'sunrise': sunrise,
            'sunset': sunset
        }
        return render(request, 'index.html', {'weather_data': weather_data})
    else:
        city = 'London'
        r = requests.get(url.format(city)).json()
        sunrise = datetime.fromtimestamp(r['sys']['sunrise'])
        sunset = datetime.fromtimestamp(r['sys']['sunset'])
        dt = datetime.fromtimestamp(r['dt'])
        weather_data = {
            'city': city,
            'temperature': r['main']['temp'],
            'temp_min': r['main']['temp_min'],
            'temp_max': r['main']['temp_max'],
            'description': r['weather'][0]['description'],
            'wind': r['wind']['speed'],
            'country': r['sys']['country'],
            'humidity': r['main']['humidity'],
            'icon': r['weather'][0]['icon'],
            'date': dt,
            'sunrise': sunrise,
            'sunset': sunset
        }
        return render(request, 'index.html', {'weather_data': weather_data})
