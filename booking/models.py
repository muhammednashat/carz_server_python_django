from django.db import models
from carzApis.models import UserModle


class BookingModel(models.Model):
    card_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(
        UserModle,
        default= '',
        on_delete= models.CASCADE, 
        related_name= 'bookings')
    car = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    
