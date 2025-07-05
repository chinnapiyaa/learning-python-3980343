#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
import shutil


# make a duplicate of an existing file
#os.rename("shell_start.py", "shell_start_renamed.py")
if path.exists(""):
  #src= path.realpath("shell_start.py")  
    # get the path to the file in the current directory
      src = path.realpath("shell_start_renamed.py")
        
    # # let's make a backup copy by appending "bak" to the name
    #  dst = src + ".bak"
    # # now use the shell to make a copy of the file

     # shutil.copy(src, dst)
    # # rename the original file
      os.rename("shell_start.py", "shell_start_renamed.py")
    
    # now put things into a ZIP archive

      root_dir , tail = path.split(src)
      shutil.make_archive("shell_start_archive", 'zip', root_dir, tail)
    # more fine-grained control over ZIP files
      