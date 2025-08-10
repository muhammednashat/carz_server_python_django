import graphene
from django.db import models
from graphene_django import DjangoObjectType
from carzApis.models import UserModle

    

class UserType(DjangoObjectType):
    class Meta:
        model = UserModle
        fields = ("id", "name", "email")


class GetUserByIdMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    user = graphene.Field(UserType)    
    
    @classmethod
    def mutate(cls,root,info,id):
        user = UserModle.objects.get(id=id)
        return cls(user = user)
        
            
class DeletUserMutatoion(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    status = graphene.Boolean()
    
    @classmethod
    def mutate(cls,root,info,id):
        try: 
           user = UserModle.objects.get(id= id)
           user.delete()
           status = True
           return cls(status = status)  
        except:
           status = False
           return cls(status = status) 

        
class UpdateUserMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        id = graphene.ID()
    user = graphene.Field(UserType)    
    
    @classmethod
    def mutate(cls,root,inf,name, id):
       user = UserModle.objects.get(id = id)
       user.name = name
       user.save()
       return cls(user = user)
    


class CreatUserMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email =graphene.String()
    user = graphene.Field(UserType)    
    
    @classmethod
    def mutate(cls, root, info, name, email):
        user = UserModle(name=name , email=email)
        user.save()
        return cls(user=user)
          
          
class Mutation(graphene.ObjectType ):
   updateUser = UpdateUserMutation.Field()
   create_user = CreatUserMutation.Field()             
   delete_user = DeletUserMutatoion.Field()
   getUserById = GetUserByIdMutation.Field()
   
    
class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(root, info):
        return UserModle.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
