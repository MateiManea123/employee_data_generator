from django.db import models
from app.services.helpers.date_helper  import first_day_of_current_month
from app.models.employee_model import Employee


class WorkDay(models.Model):
    month = models.DateField(default=first_day_of_current_month)
    working_days = models.IntegerField(null=False)
    vacation_days = models.IntegerField(null=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name="workday")
    def __repr__(self):
       return f"WorkDay<month: {self.month}, working_days:{self.working_days}, vacation_days:{self.vacation_days}"