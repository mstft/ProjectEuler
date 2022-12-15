"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# For this question I used datetime lib which I can control 
# name of day and day of month easily.
import datetime

# Start day is 1-1-1901
day_of_calendar = datetime.date(1901, 1, 1)
# End is 12-31-200
last_day = datetime.date(2000, 12, 31)

# count will increase by one if first day of month is Sunday
count = 0

while day_of_calendar <= last_day:
    # If first day of month (day==1) is Sunday (isoweekday() == 7)
    if (day_of_calendar.isoweekday() == 7) and (day_of_calendar.day == 1):
        count += 1
    # check next day
    day_of_calendar += datetime.timedelta(1)
    
print(f"Solution for Question_19 is {count}") 