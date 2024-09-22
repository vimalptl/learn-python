#Using module
# Modules are Python files with .py extension
# You can import specific functions from a module
from time import asctime, sleep  
print("Start Time: " + asctime())
sleep(1)
print("End Time: " + asctime())

import time #will bring in everything in time vs just getting the functions you waant
print(dir(time)) #will list all the functions in time module

import sys
for path in sys.path:
    print(path)

# Python Modules has a large set of libraries that you can import
# You want to first see what python has in its standard library before 
# writing your own library:  https://docs.python.org/3/library/index.html

filename = 'test.txt'
try:
    # Open file and print to screen each line
    with open(filename) as test_file:
        for line in test_file:
            print(line) 
except FileNotFoundError:
    print("File not found: " + filename)
    sys.exit(1)

#My Module Example.  What's wrong with this example below?
import say_hi as sayHi  
sayHi.say_hi("Vimal")