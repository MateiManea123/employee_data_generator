from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import mm
from datetime import datetime


def draw_section_title(c, title, x, y):
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.darkblue)
    c.drawString(x, y, title)
    c.setFillColor(colors.black)
    c.setLineWidth(0.3)
    c.line(x, y - 2, x + 520, y - 2)
def make_pdf_template(employee):
    cas = 25 / 100 * employee.salary.get().base_value
    cass = 10/100*employee.salary.get().base_value
    income_tax = 10/100*(employee.salary.get().base_value - cas - cass)
    total_deduction = cas+cass+income_tax
    c = canvas.Canvas(f"employee_pdfs/{employee.last_name}_{employee.first_name}_salary_slip_{datetime.now():%Y-%m}.pdf", pagesize=A4,encrypt=f"{employee.cnp}")
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.HexColor("#003366"))
    c.drawString(40, height - 50, "Salary Slip")
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.black)
    c.drawString(40, height - 65, "Generated on: " + datetime.now().strftime("%d %B %Y"))

    # Employee Info Section
    draw_section_title(c, "Employee Details", 40, height - 90)
    employee_info = [
        ["Name:", f"{employee.first_name} {employee.last_name}"],
        ["Employee ID:", f"{employee.employee_code}"],
        ["Position:", f"{employee.role}"],
        ["Manager:", f"{employee.manager}"],
    ]
    emp_table = Table(employee_info, colWidths=[120, 300])
    emp_table.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, -1), "Helvetica", 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    emp_table.wrapOn(c, 0, 0)
    emp_table.drawOn(c, 40, height - 230)

    # Salary Breakdown
    draw_section_title(c, "Salary Breakdown", 40, height - 260)
    salary_data = [
        ["Component", "Amount (RON)"],
        ["Base Salary", f"{employee.salary.get().base_value}"],
        ["Days Worked", f"{employee.workday.get().working_days+employee.workday.get().vacation_days}"],
        ["Meal Tickets", f"{30*(employee.workday.get().working_days+employee.workday.get().vacation_days)}"],
        [f"{employee.bonus.get().type} Bonus", f"{employee.bonus.get().value}"],
    ]
    salary_table = Table(salary_data, colWidths=[120, 100])
    salary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONT", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
    ]))
    salary_table.wrapOn(c, 0, 0)
    salary_table.drawOn(c, 40, height - 380)

    # Deductions
    draw_section_title(c, "Deductions", 300, height - 260)
    deductions_data = [
        ["Type", "Amount (RON)"],
        ["CAS (25%)", f"{cas}"],
        ["CASS (10%)", f"{cass}"],
        ["Income Tax (10%)", f"{income_tax}"],
    ]
    deductions_table = Table(deductions_data, colWidths=[150, 100])
    deductions_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONT", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
    ]))
    deductions_table.wrapOn(c, 0, 0)
    deductions_table.drawOn(c, 310, height - 380)

    # Summary
    draw_section_title(c, "Summary", 40, height - 420)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, height - 440, "Total Earnings:")
    c.drawRightString(200, height - 440, f"{employee.salary.get().base_value}")
    c.drawString(40, height - 460, "Total Deductions:")
    c.drawRightString(200, height - 460, f"{total_deduction}")
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(colors.green)
    c.drawString(40, height - 490, "Net Salary:")
    c.drawRightString(200, height - 490, f"{employee.salary.get().base_value-total_deduction}")
    c.setFillColor(colors.black)

    # Save PDF
    c.save()