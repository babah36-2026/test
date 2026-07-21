from datetime import datetime
def get_days_from_today(input_date): 
       
    return (datetime.today().date() - datetime.strptime(input_date, "%Y-%m-%d").date()).days  

