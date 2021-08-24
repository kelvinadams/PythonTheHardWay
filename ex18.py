# Python the Hard Way - Exercise 18

# function to receive and print 2 arguments - unnecessary lines to unpack the arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# another example of how to program the first function


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# function that takes and prints 1 argument


def print_one(arg1):
    print(f"arg1: {arg1}")

# function that takes no arguments and prints out a statement


def print_none():
    print("I got nothin'.")


print_two("Kelvin", "Adams")
print_two_again("Kelvin", "Adams")
print_one("Ta da!")
print_none()
