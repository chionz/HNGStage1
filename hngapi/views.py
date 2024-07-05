from django.shortcuts import render

from django.http import JsonResponse
import requests

def get_location(ip):
    response = requests.get(f"http://ipinfo.io/105.120.132.47/json")
    data = response.json()
    print(data)
    return data["city"]

def get_temperature(location):
    api_key = '29b45c842ed4934f6f1d300c8cf894b0'
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric")
    data = response.json()
    return data["main"]["temp"]

def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Visitor')
    client_ip = request.META.get('REMOTE_ADDR')

    location = get_location(ip=client_ip)
    temperature = get_temperature(location)

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }

    return JsonResponse(response)

