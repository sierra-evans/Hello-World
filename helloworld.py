from datetime import datetime

def display_hello_world():
    print("Hello world!")
    return

def get_date(now):
    current_date = now.date()
    return current_date

def get_time(now):
    current_time = now.strftime("%H:%M")
    return current_time

def display_datetime(date, time):
    print(f"The current date is: {date}\nThe current time is: {time} MST")
    return

def main():
    display_hello_world()
    now = datetime.now()
    date = get_date(now)
    time = get_time(now)
    display_datetime(date, time)

main()