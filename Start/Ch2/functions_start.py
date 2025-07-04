# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
#def greet_fun():
 #   print("hello world!")
  #  name = input("What is your name? ")
   # print("Nice to meet you,", name)
    #lastname = input("what is your last name?")
    #print("thank you for sharing", name+" "+lastname)
#greet_fun()
# function that takes parameters
#def greet_fun(greeting):
 #   print("hello world!")
   # name = input("What is your name? ")
    #print(greeting,name)
#greet_fun("how are you")
#greet_fun("whats up")

# function that returns a value
#def double_it(X):
 # return X*2
#result = double_it(5)
#print("result is",result)

# function with default value for an parameter
#def greet_fun(greeting, name=None):
 #  print("hello world!")
  # if name == None:
   #    name = input("what is your name")
   #print(greeting,name)
   # print("Nice to meet you,", name)
    #lastname = input("what is your last name?")
    #print("thank you for sharing", name+" "+lastname)
#greet_fun(name="apoo", greeting="hey")
#greet_fun("how are you")

# function with variable number of parameters
def multi_Add(*args):
    result = 0
    for x in args:
        result = result + x
    return result
    print(multi_Add(1,2,3,4,5))
