import json
import requests

from dateutil import parser
from django.test import Client, TestCase
from django.utils.timezone import make_aware

from expenses.models import Employee, Expense


class BaseConfig(TestCase):

    @classmethod
    def setUpClass(cls):

        # We need to first run setUpClass function that we
        # inherited from TestCase.
        super(BaseConfig, cls).setUpClass()

        # Set up test client for all test classes
        # that will inherit from this class.
        cls.client = Client()

    @classmethod
    def query(cls, query: str = None):
        # Method to run all queries and mutations for tests.
        body = dict()
        body['query'] = query
        response = cls.client.post(
            '/api', json.dumps(body), content_type='application/json')
        json_response = json.loads(response.content.decode())
        return json_response

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
