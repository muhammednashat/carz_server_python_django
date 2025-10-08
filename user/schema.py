
import graphene
from graphene_django import DjangoObjectType

from carzApis.models import UserModel
from user.models import AddressModel, PaymentMethod

class PaymentMethodType(DjangoObjectType):
    class Meta:
      model = PaymentMethod
      fields = "__all__"
      

class AddressType(DjangoObjectType):
    class Meta:
        model = AddressModel
        fields = "__all__"


class AddingPaymentMethod(graphene.Mutation):
    class Arguments:
        user_id = graphene.String(required=True)
        holder_name = graphene.String(required=True)
        last_4_digits = graphene.String(required=True)
        expiry_month = graphene.String(required=True)
        expiry_year = graphene.String(required=True)
        card_type = graphene.String(required=False)

    status = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, user_id, holder_name, last_4_digits, expiry_month, expiry_year, card_type=None):
        try:
            user = UserModel.objects.get(pk=user_id)
            PaymentMethod.objects.create(
                user=user,
                card_holder_name=holder_name,
                last4_digits=last_4_digits,
                expiry_month=expiry_month,
                expiry_year=expiry_year,
                card_type=card_type or PaymentMethod.CardType.OTHER,
            )
            return cls(status=True)
        except UserModel.DoesNotExist:
            return cls(status=False)

    
    
    
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
    add_payment = AddingPaymentMethod.Field()
     
    
class Query(graphene.ObjectType):
    addresses = graphene.List(AddressType,user_id= graphene.String())
    user_payments = graphene.List(PaymentMethodType , user_id = graphene.String())
    
    def resolve_addresses(root, info, user_id):
        user = UserModel.objects.get(pk = user_id)
        return AddressModel.objects.filter(user = user)   
    
    def resolve_user_payments(root, info, user_id):
        user =  UserModel.objects.get(pk = user_id)
        return user.payment_methods.all()
          