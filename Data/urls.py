from django.urls import path
from Data import views

urlpatterns = [
    path('',views.index,name='index'),
    path('getGdpData/',views.gdpData,name='gdp'),
    path('convert_price/',views.convert_price,name='convert_price'),
    
]