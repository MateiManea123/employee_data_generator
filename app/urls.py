from django.urls import path

from .controller import views

urlpatterns= [
    path("createAggregatedEmployeeData", views.create_aggregated_employee_data, name="createExcel"),
    path("sendAggregatedEmployeeData", views.send_aggregated_employee_data, name="sendExcel"),
    path("createPdfForEmployees", views.create_pdf_to_employees, name="createPdf"),
    path("sendPdfToEmployees", views.send_pdf_to_employees, name="sendPdf")
]