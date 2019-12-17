import graphene

from graphene_django.filter import DjangoFilterConnectionField

from expenses.models import Expense
from expenses.schema.expenses_schema import ExpensesType
from utilities.object_manager import get_model_object




class Query(graphene.ObjectType):
    expenses = graphene.List(ExpensesType)

    expense = graphene.Field(
        lambda: graphene.List(
            ExpensesType), amount=graphene.Int(),
        description=graphene.String(), currency=graphene.String(),
        employee_id=graphene.String(), uuid=graphene.String())

    filter_expenses = DjangoFilterConnectionField(ExpensesType)

    def resolve_expense(self, info, **kwargs):
        uuid = kwargs.get('uuid')
        resolved_value = get_model_object(Expense, 'uuid', uuid)

        return (resolved_value,)

    def resolve_expenses(self, info, **kwargs):
        resolved_value = Expense.objects.all()

        return resolved_value

    def resolve_filter_expenses(self, info, **kwargs):
        resolved_value = Expense.objects.filter(**kwargs).order_by('uuid')

        return resolved_value
