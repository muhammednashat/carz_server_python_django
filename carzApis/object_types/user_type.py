


from graphene_django import DjangoObjectType
from carzApis.models.user_model import UserModle


class UserType(DjangoObjectType):
    class Meta:
        model = UserModle
        fields = ("id", "name", "email")