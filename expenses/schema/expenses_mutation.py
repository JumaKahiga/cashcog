import graphene

from expenses.models import Expense
from expenses.schema.expenses_schema import ExpensesType
from utilities.object_manager import (
    SaveContextManager, get_model_object)


class UpdateExpense(graphene.Mutation):
    expense = graphene.Field(ExpensesType)
    message = graphene.String()

    class Arguments:
        uuid = graphene.String(required=True)
        approved = graphene.Boolean()

    def mutate(self, info, **kwargs):
        uuid = kwargs.get('uuid')
        current_status = kwargs.get('approved')
        expense = get_model_object(Expense, 'uuid', uuid)

        if current_status == expense.approved:
            message = "No changes made. Current approval status is {}".format(current_status) # noqa

            return UpdateExpense(expense=expense, message=message)

        for (key, value) in kwargs.items():
            setattr(expense, key, value)

        with SaveContextManager(expense, model=Expense) as expense:
            pass

        message = "Approval status changed to {}".format(current_status)

        return UpdateExpense(expense=expense, message=message)


class Mutation(graphene.ObjectType):
    update_expense = UpdateExpense.Field()
