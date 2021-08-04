# Python the Hard Way - Exercise 10

# Declaring variables with strings demonstrating using escape sequences
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass 
"""
# Some variety there on Line 11
# Note: a "#" at the end of lines 7-11 would be included in the string until the final """ closes it

# Printing the strings
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
