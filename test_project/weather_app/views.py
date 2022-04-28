from django.shortcuts import render
from django.http import JsonResponse
from weather_app.models import Weather

def index(request):
    return render(request, "index.html")

def weather():
    weather = Weather.objects.all().values("si", "time", "condi", "temp", "humidity", "rainratio", "uv")
    res = []
    for w in weather:
        dic = {}
        dic["si"] = w.si
        dic["time"] = w.time
        dic["condi"] = w.condi
        dic["temp"] = w.temp
        dic["humidity"] = w.humidity
        dic["rainratio"] = w.rainratio
        dic["uv"] = w.uv
        res.append(dic)

    return JsonResponse(res)