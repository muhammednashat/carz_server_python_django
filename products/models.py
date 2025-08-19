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
        TOYOTA = "toy", _("Toyota")
        HONDA = "hon", _("Honda")
        FORD = "for", _("Ford")
        BMW = "bmw", _("BMW")
        MERCEDES = "mer", _("Mercedes-Benz")
        AUDI = "aud", _("Audi")
        VOLKSWAGEN = "vw", _("Volkswagen")
        HYUNDAI = "hyu", _("Hyundai")
        NISSAN = "nis", _("Nissan")
        TESLA = "tes", _("Tesla")
        
    class TransmissionOptions(models.TextChoices):
        MANUAL = "man", _("Manual")
        AUTOMATIC = "aut", _("Automatic")
        SEMI_AUTOMATIC = "sem", _("Semi-Automatic")
        CVT = "cvt", _("CVT")  
        DCT = "dct", _("Dual-Clutch Transmission")   
        
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
    
    
    is_trend = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)  
    can_connect_bluetooth = models.BooleanField(default=False)
    is_automatic = models.BooleanField(default=False)


