from sys import argv

script,filename = argv

print(f"We are going to erase {filename}!")
print("If you dont want that , hit CTRL_C (^C)")
print("If you want to continue , hit RETURN")

input("?")

print("opening the file ...")
target = open (filename, 'r+')
print ("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"New file looks like :")
target.close()

#t1 = target.read()
target = open (filename, 'r')
if target.mode == 'r':
#target = open (filename, 'r')
	print(target.read())
print("And finally, we close it.")
#targetr.close()
target.close()