from sys import argv

script,user_name,age = argv
#prompt = '> '
ask = '> '

print (f"Hi {user_name} of {age} years, I'm the {script} script.")
print ("I'd like to ask few more questions. ")
print (f"Do you like me {user_name}")
likes = input(ask)

print(f"where do you live {user_name}")
lives = input (ask)

print(f"what kind of computer do you have")
computer = input(ask)

print(f"So you said {likes} about liking me . You live in {lives} . Not sure what that means , though i understand you have {computer} computer . .. Nice" )

vlan-raw-device