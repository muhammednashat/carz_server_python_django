import graphene
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
class SignInMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        lang = graphene.String()    
        
        
    status = graphene.Boolean()
    msg = graphene.String()
    user = graphene.Field(UserType)
    
    @classmethod
    def mutate(cls,root, info, email, lang):
        try:
           user = UserModle.objects.all().get(email = email)
           if(user):
              print("of")  
              return cls(status = True , msg = "ok", user = user)
           else:
              print("oe")  
              return cls(status = True , msg = "ok")
                   
        except Exception as e:
           print(e)  
           return cls(status = False, msg = "null")
       
        

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
   signIn= SignInMutation.Field()
    
class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    sign_in = graphene.Field(UserType, email = graphene.String())
    
    def resolve_sign_in(root, inf, email):
        print(f"signIn => {email}")
        user = UserModle.objects.all().get(email = email)
        print(f"user {user}")
        return user
        
    def resolve_users(root, info):
        return UserModle.objects.all()


