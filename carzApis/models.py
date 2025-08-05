from django.db import models
    
 
class UserModle(models.Model):
    name = models.CharField(max_length=250)
    
class UserProfile(models.Model):
     name = models.CharField()
     email = models.EmailField(unique= True)
     
     def __str__(self):
        return f'name = {self.name} and email = {self.email}'
                