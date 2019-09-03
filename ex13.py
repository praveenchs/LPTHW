# Variables,paramters and unpacking

# import module sys , argv = argument variable . This variable holds the argument you pass to python script
from sys import argv

#unpacks argv , rather than holding all the argument . its assigned to 4 variables .
script , first , second , third = argv
a = input ("mention the color for the dess: ")

print ("The Script is called:", script)
print ("The first variable is called:" , first)
print ("The second variable is called:" , second)
print (third)
print (f"I think the color {a} suits you")