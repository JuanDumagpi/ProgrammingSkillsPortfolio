# -*- coding: utf-8 -*-
"""
print Date & Time
"""
import datetime
from datetime import date
now = datetime.datetime.now()
today = date.today()

print("It is now" ,now)
print("Year" ,today.year)
print("Month" ,today.month)
print("Day" ,today.day)
