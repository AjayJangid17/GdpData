from django.shortcuts import render
from .models import Gdp_Data,Usd_data
from django.http import JsonResponse
import requests
import json
# Create your views here.
# 

def index(request):  
    return render(request,'index.html')

def gdpData(request):  
    response = {}
    try:
        data = Gdp_Data.objects.filter().values() # Indian gpd prices model
        usd_data = Usd_data.objects.filter().values() # converted GDP prices in UDS 

        prices = {}
        c_prices = []

        '''if block is to convert the price only once and 
        stoing into Database to avoid hitting api mutiple times'''

        if len(usd_data) <= 0:
            prices = data.values_list('price',flat=True)            
            converted_prices = convert_price(prices)

            if converted_prices['status'] == 'success':
                for p in converted_prices['price']:
                    Usd_data.objects.create(price=p)
                c_prices = converted_prices['price']
        else:
            prices = data
            c_prices = Usd_data.objects.filter().values_list('price',flat=True)
            
        response['data'] = list(prices)
        response['converted_price'] = list(c_prices)
        response['status'] = 'success'
        
    except Exception as err:
        print(err)
        response['data'] = []
        response['status'] = 'failed'

    return JsonResponse({"response": response}) 


def convert_price(price_lst):
    print(price_lst,type(price_lst))
    FROM = 'INR'
    TO = "USD"
    converted_price = []

    response = {}
    try:
        if price_lst:
            for price in price_lst:
                url = f"https://api.apilayer.com/fixer/convert?to={TO}&from={FROM}&amount={price}"            
                payload = {}
                headers= {
                    "apikey": "tl2ihlLilAz0JvFjFvo2qLa3nqE4r9bF"
                }
                url_response = requests.request("GET", url, headers=headers, data = payload)

                status_code = url_response.status_code

                if status_code == 200:
                    result = json.loads(url_response.text)
                    converted_price.append(result['result'])
                print('converting')
            # print(converted_price)
            response['price'] = converted_price
            response['status'] = 'success'

    except Exception as err:
        response['price'] = converted_price
        response['message'] = err
        response['status'] = 'failed'

    # print('response',response)
    return response

    


