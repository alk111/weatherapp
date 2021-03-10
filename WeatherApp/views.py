from django.shortcuts import render
from django.http import HttpResponse
from .config.remote import getUrl
import requests
from .forms import LocationForm 
# Create your views here.
def index(request):
    location = "London,uk";

    if(request.method=="POST"):
        
        form = LocationForm(request.POST)

        if(form.is_valid()):
            location = form.cleaned_data["location"]

    apiUrl = getUrl("weather","metric") + location;
    forecastUrl = getUrl("forecast","metric") + location;

    response = requests.get(apiUrl);
    forecastResponse = requests.get(forecastUrl);

    if(forecastResponse.status_code==200):

        content = forecastResponse.json();

        forecastList = content["list"];

        selectedForecast=[];

        for i in range(0,3):

            forecastData={
                "time":forecastList[i]["dt"],
                "temp":forecastList[i]["main"]["temp"],
                "weather":forecastList[i]["main"]
            }

            selectedForecast.append(forecastData);
    else:
        selectedForecast=null;


    if(response.status_code==200):
        content = response.json();

        weather = content["weather"][0]["description"]
        temp = content["main"]["temp"]
        country = content["sys"]["country"]
        name = content["name"]
        icon = content["weather"][0]["icon"]

        context = {
            "weather":weather,
            "temp":temp,
            "country":country,
            "name":name,
            "icon":icon
        }

    else:
        context={}
        
    context["form"] = LocationForm()

    context["selectedForecast"]=selectedForecast;

    return render(request,'index.html',context)