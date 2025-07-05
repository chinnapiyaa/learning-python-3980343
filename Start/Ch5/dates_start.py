#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
#print("today's date is:", today)

# print out the date's individual components
#print("date components:",today.year, today.month, today.day)

# retrieve today's weekday (0=Monday, 6=Sunday)
#print("today's weekday #:", today.weekday())
#days=["mon","tue","wed","thu","fri","sat","sun"]
#print("which is a:", days[today.weekday()])

## DATETIME OBJECTS
# Get today's date from the datetime class
#today2 = datetime.now()
#print("today's date is:",today2)

# Get the current time
t= datetime.time(datetime.now())
print("the current time is:",t)