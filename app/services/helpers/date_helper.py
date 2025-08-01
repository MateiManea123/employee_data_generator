from datetime import datetime, date

def first_day_of_current_month():
    today = datetime.today()
    return date(today.year, today.month, 1)