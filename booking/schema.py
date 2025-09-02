import graphene

from graphene_django import DjangoObjectType

from booking.models import BookingModel
from carzApis.models import UserModel

class BookingType(DjangoObjectType):
    class Meta:
        model = BookingModel
        fields ="__all__"

class Query(graphene.ObjectType):
    
    user_bookings = graphene.List(BookingType, user_id = graphene.ID())
    
    def resolve_user_bookings(root, info, user_id):
        user = UserModel.objects.get(pk= user_id)
        bookings = BookingModel.objects.all().filter(user = user)
        
        return bookings
       

class BookingMutaion(graphene.Mutation):
    class Arguments:
        card_number = graphene.String()
        address = graphene.String()
        user_id = graphene.String()
        car = graphene.String()
        date = graphene.String()
        time = graphene.String()
        
    status = graphene.String()
       
    @classmethod
    def mutate(cls, root, info, card_number,address,car, user_id, date, time):
        try:    
          user = UserModel.objects.get(pk = user_id)
          booking = BookingModel(address = address ,car= car,card_number = card_number,user = user)
          booking.save()
          status = ""
        except  Exception as ee:
          print(str(ee))             
          status = str(ee)
        return cls(status = status)  
        
        
class Mutation(graphene.ObjectType):
     booking = BookingMutaion.Field()
                