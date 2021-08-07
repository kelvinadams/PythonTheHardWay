# Python the Hard Way - Exercise 15

# This exercise reads and prints out a .txt file

from sys import argv
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

# asks for the file name again and prints it
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())

# Closes the text files
txt.close()
txt_again.close()
