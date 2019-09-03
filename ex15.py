# using function called arugment (argv) from the package sys
from sys import argv 

#mapping arguments against vars script and file
script , file =argv
#mapping file object against vars called content in read mode . do python3 -m pydoc open for more options (access mode)
content = open(file,'r')
#print format , where we print a string including a var named file
print(f"Here's the content of your file {file}")
# reading and printing the content of the file object called "content" upto 10 bytes . if no value specified it will print values upto 4096 bytes or 4KB.
print(content.read(10))
print(content.closed)
content.close()
print(content.closed)

# print(f"Type the filename again:")
# file_again = input ("> ")

# txt_again = open(file_again)
# print(txt_again.read())