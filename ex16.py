# Python the Hard Way - Exercise 16

# simple example of text editing in Python
from sys import argv

script, filename = argv

# prompts the user whether they want to erase the chosen file
print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

# opens and truncates the file
print("Opening the file...")
target = open(filename, 'w')  # opens in write mode

print("Truncating the file. Goodbye!")
target.truncate()

# Prompts user to add 3 new lines to the file before closing
print("Now I'm going to ask you to type three lines of text.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Ok, now I'll write those to the file.")

target.write(f"{line1} \n{line2} \n{line3}")

print("And finally, we close it.")
target.close()
