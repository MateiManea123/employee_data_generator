import xlsxwriter

from datetime import datetime

def make_excel_template(employee):
    workbook = xlsxwriter.Workbook(f"manager_excels/{employee.first_name}_{employee.last_name}_employees_{datetime.now():%Y-%m}.xlsx")
    worksheet = workbook.add_worksheet(f"Your employees")
    worksheet.write(0,0,"#")
    worksheet.write(0,1,"First Name")
    worksheet.write(0,2,"Last Name")
    worksheet.write(0,3,"Salary to be paid")
    worksheet.write(0,4,"Working Days")
    worksheet.write(0,5,"Vacation Days")
    worksheet.write(0,6,"Additional bonuses")
    index = 1
    for subordinate in employee.subordinates.all():
        worksheet.write_row(index,0,
                            [index,
                             subordinate.first_name,
                             subordinate.last_name,
                             subordinate.salary.get().base_value,
                             subordinate.workday.get().working_days,
                             subordinate.workday.get().vacation_days,
                             subordinate.bonus.get().value])
        index+=1
    worksheet.set_column(1,6,30)
    workbook.close()