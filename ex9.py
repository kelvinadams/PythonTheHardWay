# Python the Hard Way - Exercise 9

# Declaring strings for days of the week and months of the year
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Printing days and months - \n character creates a new line
print("Here are the days: ", days)
print("Here are the months: ", months)

# Illustrating the effect of using three double-quotes """
# Each line is printed on a new line without using the \n character
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines...5...6...anything we like!
""")

# How about three single quotes? - Yep, that works too!
print('''
It would only make sense.
If we could do this with single quotes too.
Will it work?
Will it fail?
Only one way to find out!
''')
