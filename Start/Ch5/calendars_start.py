#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
#thestr = c.formatmonth(2026, 5, 0 , 0 )
#print(thestr)
# create an HTML formatted calendar

#HC = calendar.HTMLCalendar(calendar.SUNDAY)
#htmlstr = HC.formatmonth(2026, 5)
#print(htmlstr)
# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
#for i in c.itermonthdays(2026,8):
 #  print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for i in calendar.month_name:
   print(i)
for i in calendar.day_name:
    print(i)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("First Fridays of 2026:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2026, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        firstfriday = weekone[calendar.FRIDAY]
    else:
        firstfriday = weektwo[calendar.FRIDAY]
    print(f"{calendar.month_name[m]}: {firstfriday}")