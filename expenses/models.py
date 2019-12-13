from django.db import models

# Create your models here.
class Expense(models.Model):
    uuid = models.CharField(max_length=250, primary_key=True)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=10)
    approved = models.BooleanField(default=False)
    employee = models.ForeignKey(
        'Employee', related_name='employee_expenses',
        on_delete=models.CASCADE)


class Employee(models.Model):
    uuid = models.CharField(max_length=250, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
