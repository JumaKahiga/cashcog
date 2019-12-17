from faker import Faker

from tests.base_config import BaseConfig
from tests.fixtures import (
    get_expense, filter_expense, get_all_expenses)


fake = Faker()


class TestFetchExpenses(BaseConfig):
    def setUp(self):
        super(TestFetchExpenses, self).setUp()

        self.expense_dict = {'uuid': self.uuid}
        self.employee_dict = {'employee_id': self.employee.uuid}

    def test_fetch_expense(self):
        response = self.query(get_expense.format(**self.expense_dict))
        response = response['data']['expense'][0]

        self.assertEqual(self.uuid, response['uuid'])

    def test_fetch_all_expenses(self):
        response = self.query(get_all_expenses)
        response = response['data']['expenses']

        self.assertEqual(1, len(response))

    def test_filter_expense(self):
        response = self.query(filter_expense.format(**self.employee_dict))
        response = response['data']['filterExpenses']['edges'][0]['node']

        self.assertEqual(self.uuid, response['uuid'])

    def test_no_result_filter(self):
        self.employee_dict['employee_id'] = fake.name()
        response = self.query(filter_expense.format(**self.employee_dict))
        response = response['data']['filterExpenses']['edges']

        self.assertEqual(0, len(response))
