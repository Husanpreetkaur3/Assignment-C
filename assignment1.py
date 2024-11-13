#!/usr/bin/env python3

'''
OPS445 Assignment 1
Script Name: assignment1.py
This script was written by "Husanpreet Kaur". The Python code in this file
is my own original work. No code in this file was copied from any external 
source except those provided by the course instructor, including any individual, 
textbook, or online resource. This Python script has not been shared with 
anyone else except for submission for grading. I understand and acknowledge 
the Academic Honesty Policy, and I understand that violations will result 
in appropriate disciplinary actions.

Author: Husanpreet Kaur
Semester: Fall 2024
Description: This script calculates an end date based on a given start date and a specified 
             number of days, then determines the day of the week for that end date.
'''

import sys


def leap_year(year: int) -> bool:
    """Determine if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """Get the maximum number of days in a given month, accounting for leap years."""
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    # Adjust February for leap years
    if month == 2 and leap_year(year):
        return 29
    return days_in_month.get(month, 0)  # Return 0 if month is invalid


def after(date: str) -> str:
    """Calculate the date of the next day for a given date in DD/MM/YYYY format."""
    day, month, year = (int(x) for x in date.split('/'))
    day += 1
    if day > mon_max(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"{day:02}/{month:02}/{year}"

def day_of_week(date: str) -> str:
    """Determine the weekday for a given date using Sakamoto's algorithm."""
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def usage():
    """Provide a usage message for the user."""
    print("Usage: assignment1.py DD/MM/YYYY NN")
    sys.exit(1)

def valid_date(date_str: str) -> bool:
    """Validate a date string in DD/MM/YYYY format."""
    try:
        day, month, year = (int(x) for x in date_str.split('/'))
        if year < 1 or month < 1 or month > 12:
            return False
        return 1 <= day <= mon_max(month, year)
    except ValueError:
        return False

def before(date: str) -> str:
    """Calculate the date of the previous day for a given date in DD/MM/YYYY format."""
    day, month, year = (int(x) for x in date.split('/'))
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = mon_max(month, year)
    return f"{day:02}/{month:02}/{year}"


def day_iter(start_date: str, num_days: int) -> str:
    """Calculates the date after moving a specified number of days from the starting date."""
    # Set the initial date to start_date
    current_date = start_date

    # Loop to iterate forward or backward depending on num_days sign
    for _ in range(abs(num_days)):
        current_date = after(current_date) if num_days > 0 else before(current_date)

    return current_date

if __name__ == "__main__":
    # Check the correct number of arguments
    if len(sys.argv) != 3:
        usage()  # Call usage if arguments are incorrect

    # Parse and validate inputs
    start_date = sys.argv[1]
    days_offset_str = sys.argv[2]
   # Validate that the start date format is correct and that days offset is an integer
    if not valid_date(start_date) or not days_offset_str.lstrip('-').isdigit():
        usage()  # Print usage if validation fails

    # Convert days offset to an integer and find the end date
    days_offset = int(days_offset_str)
    end_date = day_iter(start_date, days_offset)

    # Get the day of the week for the end date
    weekday_name = day_of_week(end_date)\

    # Display the result
    print(f"The end date is {weekday_name}, {end_date}.")
