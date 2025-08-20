from django.contrib import admin

from products.models import CarModel , BrandModel

admin.site.register([CarModel , BrandModel])
