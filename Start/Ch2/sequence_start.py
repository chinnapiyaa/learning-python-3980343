# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylistex = [1, 2, 4, "abc", "%$S", 3.14, True]
#print(mylistex)
#print(type(mylistex))
#print(len(mylistex))

# to access a member of a sequence type, use []
print(mylistex[3])
print(mylistex[-3])
mylistex[0]= 100


# add a list to another list


# use slices to get parts of a sequence
print(mylistex[1:4])

# you can use slices to reverse a sequence

print(mylistex[::-3])

# Tuples are like lists, but they are immutable

mytuples =(0,1,2,"three")
#print(mytuples[1])
# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, "abc", "%$S", 3.14, True}
print(myset)
# Set, however, can not be indexed like lists or tuples

#print(myset[0]) # this will cause an error

# Test for membership
print( 1 in myset)
print( 3 in mytuples)