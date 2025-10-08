from django.contrib import admin

from user.models import AddressModel, PaymentMethod

# Register your models here.

admin.site.register([AddressModel, PaymentMethod])