import datetime
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.services.email.email_maker_excel import make_email_excel
from app.services.email.email_maker_pdf import make_email_pdf
from app.services.exceptions.exceptions import FileNotReadyError
from app.services.generators.archive_generator import check_and_add_to_archive
from app.services.generators.excel_generator import generate_employees_excel
from app.services.generators.pdf_generator import generate_employees_pdf


# Create your views here.

@api_view(["POST"])
def create_aggregated_employee_data(request):
    generate_employees_excel()
    return Response(
        "Generated all Excel files!",status=status.HTTP_200_OK
    )


@api_view(["POST"])
def send_aggregated_employee_data(request):
    try:
        make_email_excel()

    except FileNotReadyError as e:
        return Response(
            {"details": str(e)},
            status = status.HTTP_409_CONFLICT
        )
    open("excel.flag", "w").close()
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    archive_path = os.path.join(base_dir, "archive", f"archive_{datetime.datetime.now():%m}.zip")
    check_and_add_to_archive(archive_path)
    return Response(
        "Sent all emails with Excels to the managers!", status=status.HTTP_200_OK
    )

@api_view(["POST"])
def create_pdf_to_employees(request):
    generate_employees_pdf()
    return Response(
        "Generated all PDF files!",
        status=status.HTTP_200_OK
    )

@api_view(["POST"])
def send_pdf_to_employees(request):
    try:
        make_email_pdf()
    except FileNotReadyError as e:
        return Response(
            {"details": str(e)},
            status=status.HTTP_409_CONFLICT
        )
    open("pdf.flag", "w").close()
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    archive_path = os.path.join(base_dir, "archive", f"archive_{datetime.datetime.now():%m}.zip")
    check_and_add_to_archive(archive_path)
    return Response(
        "Sent all emails with PDFS to the employees!", status=status.HTTP_200_OK
    )