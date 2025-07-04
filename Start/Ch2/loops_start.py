# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


#x = 0

# define a while loop

#while x < 5:
 # print(x)
  #x = x+1
 # answer = input ("should i stop?")
  #while answer !="yes":
   # print(answer)
    #answer = input("should i stop?")
# define a for loop
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#for daynames in days:
 # print(daynames)

# use a for loop over a collection


# use the break and continue statements

#for d in days:
 # if( d == "Thu"):
  #  break # to skip the rest of the loop
  #print(d)
#for d in days:
 # if( d == "Thu"):
  #  continue # to skip just the "thu" and continue with the rest of the loop#
  #print(d)

# using the enumerate() function to get an index and an item
for i , d in enumerate(days):
    print(i,d)