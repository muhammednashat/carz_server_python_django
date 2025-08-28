from django.contrib import admin

from carzApis.models import UserModel, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserModel)
