from django.db import models
from app.services.helpers.date_helper  import first_day_of_current_month
from app.models.employee_model import Employee


class Bonus(models.Model):
    type = models.CharField(max_length=200,choices=[("Performance", "Performance"),
                                                    ("Holidays", "Holidays"),
                                                    ("Certification", "Certification"),
                                                    ("Referral", "Referral"),
                                                    ("Loyalty", "Loyalty")],null=True)
    month = models.DateField(default=first_day_of_current_month)
    value = models.IntegerField(default=0)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE, default=1,null=False,related_name="bonus")