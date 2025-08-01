from django.db import models
from app.services.helpers.date_helper  import first_day_of_current_month
from app.models.employee_model import Employee


class Salary(models.Model):
    month = models.DateField(default=first_day_of_current_month)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, null=False,related_name="salary")
    base_value = models.IntegerField(default=0)