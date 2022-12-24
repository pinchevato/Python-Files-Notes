#!/usr/bin/python3
# Import the os module
import os

# Assign the output of os.uname() to the the systemInfo variable
# os.uname() returns a 5-string tuple (sysname, nodename, release, version, machine)
# Documentation: https://docs.python.org/3.2/library/os.html#module-os
systemInfo = os.uname()

# This is a fixed array with the desired captions in the script output
headers = ["Operating system","Hostname","Release","Version","Machine"]

# Initial value of the index variable. It is used to define the
# index of both systemInfo and headers in each step of the iteration.
index = 0

# Initial value of the caption variable.
caption = ""

# Initial value of the values variable
values = ""

# Initial value of the separators variable
separators = ""

# Start of the loop
for item in systemInfo:
    if len(item) < len(headers[index]):
   	 # A string containing dashes to the length of item[index] or headers[index]
   	 # To repeat a character(s), enclose it within quotes followed
   	 # by the star sign (*) and the desired number of times.
   	 separators = separators + "-" * len(headers[index]) + " "
   	 caption = caption + headers[index] + " "
   	 values = values + systemInfo[index] + " " * (len(headers[index]) - len(item)) + " "
    else:
   	 separators = separators + "-" * len(item) + " "
   	 caption =  caption + headers[index] + " " * (len(item) - len(headers[index]) + 1)
   	 values = values + item + " "
    # Increment the value of index by 1
    index = index + 1
# End of the loop

# Print the variable named caption converted to uppercase
print(caption.upper())

# Print separators
print(separators)

# Print values (items in systemInfo)
print(values)

# INSTRUCTIONS:
# 1) Save the script as uname.py (or another name of your choosing) and give it execute permissions:
# chmod +x uname.py
# 2) Execute it:
# ./uname.py
