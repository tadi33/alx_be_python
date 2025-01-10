from datetime import datetime, timedelta

current_datetime = datetime.now()
print(f'Current date and time: {current_datetime}')
add_day = input("Enter the number of days to add to the current date: ")
def display_current_datetime():
    days_to_add = int(add_day)
    future_date = current_datetime + timedelta(days=days_to_add)
    return future_date

future_date = display_current_datetime()
print(f"Future date: {future_date}")