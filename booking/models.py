from django.db import models
from carzApis.models import UserModel


class BookingModel(models.Model):
    date = models.CharField()
    time = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(
        UserModel,
        default= '',
        on_delete= models.CASCADE, 
        related_name= 'bookings'
        
        )
    car = models.CharField(max_length=200)
    
