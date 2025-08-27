from django.db import models
from django.utils.translation import gettext_lazy as _




class CarModel(models.Model):
    class FuelType(models.TextChoices):
        PETROL = "pet", _("Petrol")
        ELECTRIC = "elc", _("Electric")
        HYBRID = "hyb", _("Hybrid")
        DIESEL = "dis", _("Diesel")
        CNG = "cng", _("CNG")
        LPG = "lpg", _("LPG")
        
    class CarType(models.TextChoices):
        ECONOMY = "eco", _("Economy")
        SEDAN = "sed", _("Sedan")
        SUV = "suv", _("SUV")
        COUPE = "cou", _("Coupe")
        HATCHBACK = "hat", _("Hatchback")
        CONVERTIBLE = "con", _("Convertible")
        PICKUP = "pic", _("Pickup Truck")
        VAN = "van", _("Van")
        LUXURY = "lux", _("Luxury")
        SPORTS = "spo", _("Sports Car")
    
    class BrandCar(models.TextChoices):
        
        HONDA = "hon", _("Honda")
        VOLKSWAGEN = "vw", _("Volkswagen")
        BMW = "bmw", _("BMW")
        AUDI = "aud", _("Audi")
        NISSAN = "nis", _("Nissan")
        FORD = "for", _("Ford")
        FRA ="fra",_("Farrari")
        LAM = "lamb", _("Lamborghini")
        MERCEDES = "mer", _("Mercedes")
        TESLA = "tes", _("Tesla")
        TOYOTA = "toy", _("Toyota")
        HYUNDAI = "hyu", _("Hyundai")
        
    class TransmissionOptions(models.TextChoices):
        MANUAL = "man", _("Manual")
        AUTOMATIC = "aut", _("Automatic")
        SEMI_AUTOMATIC = "sem", _("Semi-Automatic")
        CVT = "cvt", _("CVT")  
        DCT = "dct", _("Dual-Clutch Transmission")   
    brandImage = models.CharField(max_length=500 , default="")    
    imgUrl = models.CharField(max_length=500, default= "") 
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    brand = models.CharField(max_length=50, choices= BrandCar , default= BrandCar.HYUNDAI)
    rating = models.IntegerField()
    transmission_options = models.CharField(max_length=100 ,choices=TransmissionOptions, default= TransmissionOptions.AUTOMATIC)
    car_type= models.CharField(max_length=50,
                                choices= CarType, default= CarType.ECONOMY)
    
    
    fuel_type = models.CharField(
        max_length=50,
        choices=FuelType,
        default=FuelType.PETROL
        )
  
    is_popular = models.BooleanField(default=False)  
    can_connect_bluetooth = models.BooleanField(default=False)
    is_automatic = models.BooleanField(default=False)

class BrandModel(models.Model):
    name = models.CharField(max_length=100)
    name_in_database = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)
    numbers = models.IntegerField(default=42) 