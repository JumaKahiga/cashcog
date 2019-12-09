import graphene

from expenses.schema import expenses_query


class Query(expenses_query.Query):
    pass


# class Mutation():
#     pass


schema = graphene.Schema(query=Query)
