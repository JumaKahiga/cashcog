import unittest
import requests

from dateutil import parser
from django.core.exceptions import FieldError
from django.utils.timezone import make_aware
from faker import Faker
from graphql import GraphQLError

from expenses.models import Employee, Expense
from utilities.object_manager import get_model_object


fake = Faker()


class TestObjectManagers(unittest.TestCase):
    def setUp(self):
        self.response = requests.get('https://cashcog.xcnt.io/single')
        self.data = self.response.json()
        self.uuid = self.data.get('uuid')

        self.employee = Employee()
        self.expense = Expense()

        for (key, value) in self.data.get('employee').items():
            setattr(self.employee, key, value)

        self.employee.save()

        self.data['employee'] = self.employee

        for (key, value) in self.data.items():
            setattr(self.expense, key, value)
        self.created_at = parser.parse(self.data.get('created_at'))
        self.created_at = make_aware(self.created_at)
        self.expense.created_at = self.created_at
        self.expense.save()

    def test_get_model_object(self):
        expense_obj = get_model_object(Expense, 'uuid', self.uuid)

        self.assertEqual(expense_obj.amount, self.data['amount'])
        self.assertIn('employee', self.data)

    def test_get_model_object_fail(self):
        """ object not found."""
        with self.assertRaises(GraphQLError):
            get_model_object(Expense, 'uuid', fake.name())

    def test_get_model_object_fail_2(self):
        """ column not found."""
        with self.assertRaises(FieldError):
            get_model_object(Expense, 'uuid2', self.uuid)
