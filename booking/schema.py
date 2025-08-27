import graphene
from models import BookingModel
from graphene_django import DjangoObjectType

class BookingType(DjangoObjectType):
    class Meta:
        model = BookingModel
        fields ="__all__"
        

class BookingMutaion(graphene.Mutation):
    class Arguments:
        card_number = graphene.String()
        address = graphene.String()
        user = graphene.ID()
        car = graphene.String()
        date = graphene.Date()
        time = graphene.Time()
    status = graphene.Boolean
       
    @classmethod
    def mutate(cls, root, info, card_number,address,user,car,date,time):
        
      pass
        
class Mutation(graphene.ObjectType):
     pass
                