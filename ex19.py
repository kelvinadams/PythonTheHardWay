# Python the Hard Way - Exercise 19

# simple, silly function example
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} kinds of cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Wow, that's enough for a party!")
    print(f"Or...a picnic. Get a blanket!\n")


# example of calling the above function
print("We can just giv ethe function numbers directly:")
cheese_and_crackers(20, 30)

# alternate example of calling the funciton using variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# example using math operators inside the function call
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

# example combining variables and math operators
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
