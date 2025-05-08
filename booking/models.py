from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Hotels(models.Model):
    #condo_id, condo_name, owner,  location, rooms
    name = models.CharField(max_length=30,default="Stary-Condohotel")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50,default="Palawan")
    country = models.CharField(max_length=50,default="Philippines")
    def __str__(self):
        return self.name


class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("available", "Available"), 
    ("not_available", "Not available"),    
    ) 

    ROOM_TYPE = ( 
    ("one_bed", "One Bed"), 
    ("two_bed", "Two Bed"),
    ("sea_wiev","Sea Wiev"),  
    ("city_wiev","City Wiev"),  
    ) 


    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1, null=True, blank=True)
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField()
    def __str__(self):
                return self.hotel.name
    

class Reservation(models.Model):
        
        check_in = models.DateField(auto_now=False)
        check_out = models.DateField()
        room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
        guest = models.ForeignKey(User, on_delete=models.CASCADE)
        
        booking_id = models.CharField(max_length=100, default="null")
        def __str__(self):
            return self.guest.username