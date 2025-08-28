from django.db import models
    
 
class UserModel(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique= True, null = True)
    
class UserProfile(models.Model):
     name = models.CharField()
     email = models.EmailField(unique= True)
     
     def __str__(self):
        return f'name = {self.name} and email = {self.email}'
                