#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall2024
Program: assignment1.py 
Author: Anthony Jaishanan Jayaratnam
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys
from datetime import datetime

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check."
    if month in [1, 3, 5, 7, 8, 10, 12]: # Months with 31 days
        return 31
    elif month in [4, 6, 9, 11]: # Months with 30 days
        return 30
    elif month == 2: # February
        return 29 if leap_year(year) else 28
    else:
        return 0  # Invalid month

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format
    Return the date for the next day of the given date in YYYY-MM-DD format.
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):  # Check if the day exceeds the month's maximum
        to_day = 1  # Reset to the first day of the next month
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12: # Check if the month exceeds December
        to_month = 1  # Reset to January
        year += 1 # Increment the year
    else:
        to_month = tmp_month

    return f"{year}-{to_month:02}-{to_day:02}"  # Return the next date in YYYY-MM-DD format

def usage():
    "Print a usage message to the user."
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def leap_year(year: int) -> bool:
    "Return True if the year is a leap year."
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def valid_date(date: str) -> bool:
    "Check validity of date and return True if valid."
    try:
        # Attempt to parse the date string in the format YYYY-MM-DD
        datetime.strptime(date, '%Y-%m-%d') # Parse the date using datetime
        return True
    except ValueError:  # Handle invalid date formats
        # If parsing fails, the date is invalid
        return False

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days."
    count = 0
    current_date = start_date
    while current_date <= stop_date:   # Loop through each date in the range
        weekday = day_of_week(*map(int, current_date.split('-')))  # Get the day of the week
        if weekday in {'sat', 'sun'}:  # Assuming 'sat' and 'sun' represent Saturday and Sunday
            count += 1
        current_date = after(current_date)
    return count

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    start_date, end_date = sys.argv[1], sys.argv[2]

    if not valid_date(start_date) or not valid_date(end_date):
        usage()

    # Ensure the start date is earlier than the end date
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    weekend_days = day_count(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {weekend_days} weekend days.")

