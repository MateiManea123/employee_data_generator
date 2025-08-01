from datetime import datetime

from app.services.email.email_sender import send_email_with_attachment
from app.models import *

all_employee_data = Employee.objects.all().prefetch_related('salary', 'workday', 'bonus')
def make_email_excel():
    subject = f"Employee Data Excel Month {datetime.now():%m}"
    body = f"Attached to this mail you will find the Employee Data Excel for {datetime.now():%m-%Y}! \n\n\n\nThank you! \nHR Team"
    from_email = "bestcompanyintheworld@gmail.com"

    for employee in all_employee_data:
        if employee.role == 'Manager':
            to_email = [f"{employee.email}"]
            file_path = f"manager_excels/{employee.first_name}_{employee.last_name}_employees_{datetime.now():%Y-%m}.xlsx"
            send_email_with_attachment(subject, body, from_email, to_email, file_path)