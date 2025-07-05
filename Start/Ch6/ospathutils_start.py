#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#


import os
from os import path
import time
from datetime import datetime
# Print the name of the OS
#print("Operating System:", os.name)

# Check for item existence and type
#print("item exists:", path.exists("textfile.txt"))
#print("item is a file:", path.isfile("textfile.txt"))
#print("item is a directory:", path.isdir("textfile.txt"))
# Work with file paths
#print("Item path:", path.realpath("textfile.txt"))
#print("Item path and name:", path.split(path.realpath("textfile.txt")))

# Get the modification time
t = time.ctime(path.getmtime("samplexml.xml"))
print("Last modified time:", t)

# Calculate how long ago the item was modified
td = datetime.now() - datetime.fromtimestamp(path.getmtime("samplexml.xml"))
print("It has been", td, "since the file was modified")
print(f"Or {td.total_seconds()} seconds")
