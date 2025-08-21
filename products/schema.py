
from graphene_django import DjangoObjectType
import graphene
from django.db.models import Q
from products.models import BrandModel, CarModel

class BrandType(DjangoObjectType):
    class Meta:
       model = BrandModel
       fields = "__all__" 
             
class CarType(DjangoObjectType):
    class Meta:
        model = CarModel
        fields = "__all__"
        
class Query(graphene.ObjectType):
    populars = graphene.List(CarType)
    rending_brands = graphene.List(CarType)
    cars_by_brand = graphene.List(CarType, brand = graphene.String())
    car_brands = graphene.List(BrandType)
    
    
    def resolve_populars(root, info):
        cars = CarModel.objects.all().filter( is_popular = True)
        return cars 

    def resolve_rending_brands(root,info):
        return CarModel.objects.filter(brand__in = ["hon","for" , "aud","tes","fra",])
             
    def resolve_cars_by_brand(root,info,brand):
        return CarModel.objects.filter(brand = brand)
    
    def resolve_car_brands(root, info,):
        return BrandModel.objects.all()
        