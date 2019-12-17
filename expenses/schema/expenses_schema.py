import graphene

from graphene_django import DjangoObjectType
from graphene.utils.resolve_only_args import resolve_only_args

from expenses.models import Expense


class ExpensesType(DjangoObjectType):
    class Meta:
        model = Expense

        filter_fields = {
            "uuid": ['exact'],
            "amount": ["exact"],
            "description": ['iexact', 'icontains', 'istartswith'],
            'currency': ['iexact'],
            "employee_id": ["exact"],

        }

        interfaces = (graphene.relay.Node, )

    uuid = graphene.ID(required=True)

    @resolve_only_args
    def resolve_uuid(self):
        return self.uuid
