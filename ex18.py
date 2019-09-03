#First we tell Python we want to make a function using def for ”define”.
#On the same line as def we give the function a name called "print_two" 
#Then we tell it we want *args (asterisk args), which is a lot like your argv parameter but for
#functions. This has to go inside () parentheses to work.
def print_two(*args):
#After the colon all the lines that are indented four spaces will become attached to this name,
#print_two. Our first indented line is one that unpacks the arguments, the same as with your
#scripts.
	args1,args2 = args
#To demonstrate how it works we print these arguments out, just like we would in a script.
	print(f"arg1: {args1}, \narg2: {args2}")

print_two("praveen","chalamalasetti")

def print_two_again(arg1,arg2):
	print(f"arg1: {arg1}, \narg2: {arg2}")

	
print_two_again("praveen_again","chalamalasetti_again")

# def is syntax for creating a function (def = define), followed by function name .
#ex: def def_name ==> def_name is the name of the function.

def print_one(arg):
	print(f"Here is the new arg :{arg}")
	
print_one("one_arg")

# this one takes no arguments

def print_none():
	print(f"There is no argument to print")
	
print_none()