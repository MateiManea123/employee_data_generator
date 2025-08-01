from app.services.template_makers.excel_template import make_excel_template
from app.models import *


def generate_employees_excel():
    all_employee_data = Employee.objects.all().prefetch_related('salary', 'workday', 'bonus')
    for employee in all_employee_data:
        if employee.role == "Manager":
            make_excel_template(employee)

