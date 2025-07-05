
#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

# Times and dates can be formatted using a set of predefined string
# control codes 
now = datetime.now()
#print("The current date is:", now)

#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
#print(now.strftime("Today's date is: %d/%m/%Y"))
#print(now.strftime("Today is: %A, %B %d, %Y"))

# %c - locale's date and time, %x - locale's date, %X - locale's time
#print(now.strftime("Locale's date and time: %c"))
#print(now.strftime("Locale's date: %x"))
#print(now.strftime("Locale's time: %X"))

#### Time Formatting ####

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("The current time is: %I:%M:%S %p"))
print(now.strftime("The current time in 24-hour format is: %H:%M:%S"))