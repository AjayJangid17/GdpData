from django.db import models

# Create your models here.



class Gdp_Data(models.Model):    
    price = models.FloatField()    
    year = models.IntegerField(default=None)

class Usd_data(models.Model):
    price = models.FloatField()    

    