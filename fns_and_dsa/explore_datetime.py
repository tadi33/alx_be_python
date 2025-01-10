from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    days_to_add = int(days_to_add)
    future_date = current_date + timedelta(days=days_to_add)
        
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date: {formatted_future_date}")
    return future_date
    
 
current_date = display_current_datetime()   
days_to_add = input("Enter the number of days to add to the current date: ")   
calculate_future_date(current_date, days_to_add)