# -*- coding: utf-8 -*-
"""
Exercise 3: Print date and Time
"""
#imports the built in library: datetime as well as the date
import datetime
from datetime import date

"""
Setting the 'now' variable using the datetime module, datetime class, and the now method.
This lets us use the current time and date into the variable as the output.
"""
now = datetime.datetime.now()
print("It is now" ,now)

"""
Placing the current date into a variable to let us use it separately for year, month and day
"""
today = date.today()

print("Year" ,today.year)
print("Month" ,today.month)
print("Day" ,today.day)
