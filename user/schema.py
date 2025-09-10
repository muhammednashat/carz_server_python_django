
import graphene
from graphene_django import DjangoObjectType

from carzApis.models import UserModel
from user.models import AddressModel

class AddressType(DjangoObjectType):
    class Meta:
        model = AddressModel
        fields = "__all__"

class AddingAddressMutaion(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        address = graphene.String()         
        user_id= graphene.String()
        
    status = graphene.Boolean()
    
    @classmethod
    def mutate(cls, root, info, title, address, user_id):
        user = UserModel.objects.get(pk = user_id)
        AddressModel(title = title, address = address, user = user).save()
        
        return cls(status = True)

class Mutation(graphene.ObjectType):
    add_address =  AddingAddressMutaion.Field()  
    
    
class Query(graphene.ObjectType):
    addresses = graphene.List(AddressType,user_id= graphene.String())
    
    def resolve_addresses(root, info, user_id):
        user = UserModel.objects.get(pk = user_id)
        return AddressModel.objects.filter(user = user)         