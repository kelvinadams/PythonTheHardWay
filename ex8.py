# Python the Hard Way - Exercise 8

# declaring the variable "formatter" as a string with open spaces to call later
formatter = "{} {} {} {}"

# prints "formatter" with the numbers 1, 2, 3, and 4 in the open "slots"
print(formatter.format(1, 2, 3, 4))
# same as above but prints words the worlds one to four
print(formatter.format("one", "two", "three", "four"))
# likewise but inserting Boolean values
print(formatter.format(True, False, False, True))
# printing spaces by calling "formatter" and creating nested list of spaces? Nope! it prints the closed curly brackets!
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Critical Role,",
    "a tale of Jester and Beau.",
    "And also their friends,",
    "but sadly the story ends."
))
