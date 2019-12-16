import json

from django.db import connection
from kafka import KafkaConsumer


class DataLoader:
    def __init__(self):
        self.keys_1 = (
            'uuid', 'description', 'created_at',
            'amount', 'currency', 'employee')

        self.keys_2 = ('uuid', 'first_name', 'last_name')

    def validate_data(self, expense):
        try:
            expense['employee']
        except KeyError:
            return False

        if all(i in expense for i in self.keys_1) and all(x in expense['employee'] for x in self.keys_2): # noqa
            return True
        else:
            return False

    def store_data(self, v_expense):
        employee_dict = v_expense['employee']
        employee_uuid = employee_dict['uuid']
        first_name = employee_dict['first_name']
        last_name = employee_dict['last_name']

        expense_uuid = v_expense['uuid']
        description = v_expense['description']
        created_at = v_expense['created_at']
        amount = v_expense['amount']
        currency = v_expense['currency']
        approved = False

        with connection.cursor() as cursor:
            cursor.execute(""" INSERT INTO
                expenses_employee (
                uuid, first_name, last_name)
                VALUES(%s, %s, %s)
                ON CONFLICT DO NOTHING""", [
                employee_uuid, first_name, last_name])

            cursor.execute(""" INSERT INTO
                expenses_expense (
                uuid, description, created_at, amount, currency, approved, employee_id)
                VALUES(%s, %s, %s, %s, %s, %s, (SELECT uuid FROM expenses_employee WHERE uuid = %s))""",
                [expense_uuid, description, created_at,
                amount, currency, approved, employee_uuid]) # noqa


if __name__ == '__main__':
    consumer = KafkaConsumer(
        'raw_expenses', bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest', enable_auto_commit=True,
        group_id='my-group', value_deserializer=lambda x: json.loads(x.decode('utf-8'))) # noqa

    dataloader = DataLoader()

    for expense in consumer:
        validated = dataloader.validate_data(expense.value)

        if validated:
            dataloader.store_data(expense.value)
