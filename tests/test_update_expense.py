from faker import Faker

from tests.base_config import BaseConfig
from tests.fixtures import update_expense


fake = Faker()


class TestUpdateExpense(BaseConfig):
    def setUp(self):
        super(TestUpdateExpense, self).setUp()

        self.expense_dict = {
            "uuid": self.uuid,
            "approved": "true"
            }

    def test_approve_expense(self):
        response = self.query(update_expense.format(**self.expense_dict))
        response = response["data"]["updateExpense"]

        self.assertEqual(True, response["expense"]["approved"])
        self.assertEqual(
            'Approval status changed to True', response["message"])

    def test_already_approved_expense(self):
        self.query(update_expense.format(**self.expense_dict))
        response = self.query(update_expense.format(**self.expense_dict))
        response = response["data"]["updateExpense"]

        self.assertEqual(
            'No changes made. Current approval status is True',
            response["message"])
