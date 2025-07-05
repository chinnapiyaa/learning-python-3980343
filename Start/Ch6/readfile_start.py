#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents
sample_file = open("basic_file.txt", "r")
if sample_file.mode == 'r':
  contents = sample_file.read()
  print(contents)
    # use the read() function to read the entire file
