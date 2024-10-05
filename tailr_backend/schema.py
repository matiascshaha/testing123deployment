import graphene
from tailr_backend.types.user_type import UserType
from tailr_backend.resolvers.user_resolver import resolve_user

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_user(self, info, id):
        return resolve_user(id)

schema = graphene.Schema(query=Query)
