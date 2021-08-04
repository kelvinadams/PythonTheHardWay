# Python the Hard Way - Exercise 6

types_of_people = 10
# This declares the variable x and assigns a string to it, already formatted with "f" in front to combine text and variables
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

# Ssame as x above
y = f"Those who know {binary} and those who {do_not}."

# printing the strings directly by calling upon the variables
print(x)
print(y)

# printing these statements that include some additional text and then call the variable that contains a string
print(f"I said: {x}")
print(f"I also said: {y}")

# setting a boolean for "hilarious"
hilarious = False
# Bad joke...also gives an open {} to be called later as ".format(____)"
joke_evaluation = "Isn't that joke funny!? {}"

# prints both the string of joke_evaluation but also invokes "hilarious" which is a boolean value of "FALSE"
print(joke_evaluation.format(hilarious))

w = "This is to the left side of..."
e = "a string with a right side."

# demonstrates that using the "+" operator on two strings (in this case called by the variables) concatenates the two
print(w+e)
