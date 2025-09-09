from django.db import models

from carzApis.models import UserModel

class AddressModel(models.Model):
    title = models.CharField()
    address = models.CharField()
    user = models.ForeignKey(
        UserModel,
        on_delete= models.CASCADE,
     
    )
    
    
