import requests
from django.shortcuts import render
from django.http import JsonResponse

# OpenWeatherMap API URL and your API key
API_KEY = '12ca7600e8f0505af0c4dd0a062a6c6f'
API_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Temperature in Celsius
    }
    response = requests.get(API_URL, params=params)
    return response.json()

def home(request):
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.POST.get('city')
        if city:
            data = get_weather_data(city)
            if data.get('cod') != 200:  # Error in response
                error_message = "City not found or invalid input!"
            else:
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                    'description': data['weather'][0]['description'],
                }
    
    return render(request, 'weather/weather.html', {'weather_data': weather_data, 'error_message': error_message})
