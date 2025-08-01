from app.models import *
from app.services.template_makers.pdf_template import make_pdf_template


def generate_employees_pdf():
    all_employee_data = Employee.objects.all().prefetch_related('salary', 'workday', 'bonus')

    for employee in all_employee_data:
        make_pdf_template(employee)