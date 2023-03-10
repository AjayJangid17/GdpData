from django.shortcuts import render
from .models import Gdp_Data
from django.http import JsonResponse
import json
# Create your views here.
# 

def index(request):  
    return render(request,'index.html')

def gdpData(request):  
    data = Gdp_Data.objects.filter().values()
    return JsonResponse({"data": list(data)})

    
