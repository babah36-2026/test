from datetime import datetime
def get_days_from_today(input_date): 
       
    return (datetime.strptime(input_date, "%Y-%m-%d").date() - datetime.today().date()).days

print(get_days_from_today("2026-07-20"))
