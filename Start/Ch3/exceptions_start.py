# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#
#x = 10/0
# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
try:
  x = 10/0
except: 
  print(" sorry it did not work")
# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
  answer = input("what should i divide 10 by")
  num = int(answer)
  print(10/num)
except ZeroDivisionError as e:
  print("you can't divide by zero")
except ValueError as e:
  print("you must enter a number")
  print(e)
finally:
  print("this is good")

# You can also catch specific exceptions

