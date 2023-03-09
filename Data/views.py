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

# data = [
# {'year':1987, 'price':283.75,},
# {'year':1988, 'price':299.65,},
# {'year':1989, 'price':300.19,},
# {'year':1990, 'price':326.61,},
# {'year':1991, 'price':274.84,},
# {'year':1992, 'price':293.26,},
# {'year':1993, 'price':284.19,},
# {'year':1994, 'price':333.01,},
# {'year':1995, 'price':366.60,},
# {'year':1996, 'price':399.79,},
# {'year':1997, 'price':423.19,},
# {'year':1998, 'price':428.77,},
# {'year':1999, 'price':466.84,},
# {'year':2000, 'price':476.64,},
# {'year':2001, 'price':493.93,},
# {'year':2002, 'price':523.77,},
# {'year':2003, 'price':618.37,},
# {'year':2004, 'price':721.59,},
# {'year':2005, 'price':834.22,},
# {'year':2006, 'price':949.12,},
# {'year':2007, 'price':1238.70,},
# {'year':2008, 'price':1224.10,},
# {'year':2009, 'price':1365.37,},
# {'year':2010, 'price':1708.46,},
# {'year':2011, 'price':1823.05,},
# {'year':2012, 'price':1827.64,},
# {'year':2013, 'price':1856.72,},
# {'year':2014, 'price':2039.13,},
# {'year':2015, 'price':2103.59,},
# {'year':2016, 'price':2294.12,},
# {'year':2017, 'price':2651.47,},
# {'year':2018, 'price':2702.93,},
# {'year':2019, 'price':2831.55,},
# {'year':2020, 'price':2667.69,},
# {'year':2021, 'price':3176.30,},
# {'year':2022, 'price':3468.57,},
# {'year':2023, 'price':3820.57,},
# {'year':2024, 'price':4170.22,},
# {'year':2025, 'price':4547.16,},
# {'year':2026, 'price':4947.39,},
# {'year':2027, 'price':5365.55,}
# ]
    
