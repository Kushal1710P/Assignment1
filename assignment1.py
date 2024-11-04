#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
"Kushal Parmar". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Kushhal Parmar
Semester: Fall 2024
Description: Date manipulation script that calculates future or past dates.
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Return true if the year is a leap year"
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    if month == 2:
        return 29 if leap_year(year) else 28
    return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format
    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    mon_max_value = mon_max(mon, year)
    if day > mon_max_value:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # Reset to first day of the next month
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # previous day

    if day < 1:
        mon -= 1
        if mon < 1:
            year -= 1
            mon = 12
        day = mon_max(mon, year)  # Get the last day of the previous month
    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "Check validity of date"
    try:
        day, month, year = (int(x) for x in date.split('/'))
        if not (1 <= day <= 31 and 1 <= month <= 12):
            return False
        if day > mon_max(month, year):
            return False
        return True
    except ValueError:
        return False

def day_iter(start_date: str, num: int) -> str:
    "Iterates from start date by num to return end date in DD/MM/YYYY"
    current_date = start_date
    for _ in range(abs(num)):
        if num > 0:
            current_date = after(current_date)
        else:
            current_date = before(current_date)
    return current_date

if __name__ == "__main__":
    # Check length of arguments
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    try:
        num_days = int(sys.argv[2])
    except ValueError:
        usage()

    # Check first argument is a valid date
    if not valid_date(start_date):
        usage()

    # Call day_iter function to get end date, save to x
    end_date = day_iter(start_date, num_days)
    print(f'The end date is {day_of_week(end_date)}, {end_date}.')
