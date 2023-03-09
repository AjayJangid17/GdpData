from django.urls import path
from Data import views

urlpatterns = [
    path('',views.index,name='index'),
    path('getGdpData/',views.gdpData,name='gdp'),
]