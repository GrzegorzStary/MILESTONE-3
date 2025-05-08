from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotels(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="Stary-Condohotel")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50,default="Palawan")
    country = models.CharField(max_length=50,default="Philippines")
    def __str__(self):
        return self.name
