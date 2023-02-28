import requests
from .models import City, District
from .forms import CityForm
from django.shortcuts import render
# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4274271153e3c4e31c8b1eab2479dd1a'
    cities = City.objects.all()
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()    
    weather_data = []
    
    for city in cities:
        try:
            city_api = url.format(city)
            r = requests.get(city_api).json()
            city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)
        except Exception as e:
            print(e)
            pass
    
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)


def city(request):
    return render(request, 'city/city.html')
