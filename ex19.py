#Variables inside function cannot be called outside the function or anywhere else in the program/script.

def cheese_and_crackers(cheese_count, boxes):
	print(f"You have {cheese_count} cheeses")
	print(f"you have {boxes} boxes to store the cheese")
	print("Man that's enough for the party!")

print("We can give the function numbers directly:")
cheese_and_crackers(3,4)

print("\nOr , we can give the variables to the function :")
amount_of_cheese=10
amount_of_box=20

cheese_and_crackers(amount_of_cheese,amount_of_box)

print("\nWe can do math as well inside")
cheese_and_crackers(4+2,5-3)

print("\nWe can math and variables: ")
cheese_and_crackers(amount_of_cheese+21,amount_of_box-13)