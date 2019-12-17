get_expense = '''
  query{{expense(uuid: "{uuid}"){{
    uuid
    description
    createdAt
    amount
    currency
    approved
  }}
  }}
'''


get_all_expenses = '''
  query{expenses{
    uuid
    description
    createdAt
    amount
    currency
    approved
  }
  }
'''


filter_expense = '''
  query{{filterExpenses(employeeId: "{employee_id}"){{
  edges{{
    node{{
        uuid
        description
        createdAt
        amount
        currency
        approved
    }}
    }}
  }}
  }}
'''


update_expense = '''
    mutation{{updateExpense(uuid: "{uuid}", approved: {approved}){{
        expense{{
            uuid
            description
            createdAt
            amount
            currency
            approved
        }}
        message
    }}}}
'''
