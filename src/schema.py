import graphene
from src.types.user_type import UserType
from src.resolvers.user_resolver import resolve_user

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_user(self, info, id):
        return resolve_user(id)

schema = graphene.Schema(query=Query)
