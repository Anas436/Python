
#Write a Python program to print the calendar of a given month and year.

import calendar

y=int(input("\nEnter your year : "))
m=int(input("\nEnter your month : "))

print(calendar.month(y,m))