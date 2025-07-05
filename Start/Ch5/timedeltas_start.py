#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
#print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
#print("today's date is:", now)

# print today's date one year from now
#print("one year from now:", now + timedelta(days=365))

# create a timedelta that uses more than one argument
#print("one week from now:", now + timedelta(weeks=2, days=3))

# calculate the date 1 week ago, formatted as a string

#t= datetime.now() - timedelta(weeks=1)
#s= t.strftime("%A, %B %d, %Y")
#print("one week ago:", s)
### How many days until April Fools' Day?
today = date.today()
afool = date(today.year,4, 1)
if today > afool:
       print(f"April Fools' Day already passed this year{(today-afool).days} days ago")
afool = afool.replace(year=today.year + 1)