from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Weather

def toDic(item):
    data = {}
    data["si"] = item.si
    data["time"] = item.time
    data["condi"] = item.condi
    data["isday"] = item.isday
    data["temp"] = item.temp
    data["humidity"] = item.humidity
    data["rainratio"] = item.rainratio
    data["snowratio"] = item.snowratio

    return data

def weather(request):
    weather = Weather.objects.all().order_by("areano", "time")
    data = []
    for i in range(len(weather)):
        data.append(toDic(weather[i]))
    weather = data

    return HttpResponse(json.dumps(weather, ensure_ascii=False), content_type = "application/json")

def index(request):
    return render(request, "index.html")