import graphene

from expenses.schema import expenses_query, expenses_mutation


class Query(expenses_query.Query):
    pass


class Mutation(expenses_mutation.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
