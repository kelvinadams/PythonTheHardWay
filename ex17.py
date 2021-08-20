# Python the Hard Way - Exercise 17

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# Reduced to 1 line from the 2-line sample
indata = open(from_file).read()

# Reports file length, checks if output file exists, and prompts the user for input to proceed or cancel
print(f"The input file is {len(indata)} bytes long.")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Opens and writes the text from input file into the output file
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done!")

# Closes the output file
out_file.close()
