
import graphene
from products import schema as product_schema
from carzApis import schema as carz_schema
from booking import schema as booking_schema

class Query(product_schema.Query, carz_schema.Query, booking_schema.Query, graphene.ObjectType):
    pass
class Mutation(carz_schema.Mutation,booking_schema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation= Mutation)
