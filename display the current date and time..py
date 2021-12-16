
#Write a Python program to display the current date and time.

import datetime

print("\nToday date and time : ")

now = datetime.datetime.now()

print(now.strftime("\n%d-%m-%y %H:%M:%S"))