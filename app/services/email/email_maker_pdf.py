from datetime import datetime
from app.services.email.email_sender import send_email_with_attachment
from app.models import *

all_employee_data = Employee.objects.all().prefetch_related('salary', 'workday', 'bonus')
def make_email_pdf():
    subject = f"Salary Slip Month {datetime.now():%m}"
    body = f"Attached to this mail you will find your salary slip for {datetime.now():%m-%Y}! \n\n\n\n\nThank you! \nPayroll Team"
    from_email = "bestcompanyintheworld@gmail.com"

    for employee in all_employee_data:
            to_email = [f"{employee.email}"]
            file_path = f"employee_pdfs/{employee.last_name}_{employee.first_name}_salary_slip_{datetime.now():%Y-%m}.pdf"
            send_email_with_attachment(subject, body, from_email, to_email, file_path)