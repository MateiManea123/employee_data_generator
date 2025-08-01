from django.contrib import admin
from .models.bonus_model import *
from .models.salary_model import *
from .models.workday_model import *
from .models.employee_model import *


# Register your models here.

admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Bonus)
admin.site.register(WorkDay)
