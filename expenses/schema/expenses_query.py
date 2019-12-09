import graphene


class HelloWorld(graphene.ObjectType):
    message = graphene.String()


class Query(graphene.ObjectType):
    response = graphene.Field(HelloWorld)

    def resolve_response(self, info, **kwargs):
        message = {"message": "Hello World"}

        return message
