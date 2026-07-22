from datetime import datetime

def get_days_from_today(input_date):   
    try:   
        return (datetime.today().date() - datetime.strptime(input_date, "%Y-%m-%d").date()).days    
    except (ValueError, TypeError):  
        return ("Неправильний формат дати, введіть дату у форматі РРРР-ММ-ДД") 
  # Example usage
