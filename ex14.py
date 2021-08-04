# Python the Hard Way - Exercise 14

# Prompting and Passing Exercise
from sys import argv
script, user_name = argv
prompt = '> '

# The kind, sensitive script asks if it is liked...
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

# Asks where the user lives
print(f"Where do you live, {user_name}?")
lives = input(prompt)

# Asks what kind of computer the user has
print("What kind of computer do you have?")
computer = input(prompt)

# Prints out a summary of the gathered input
print(f"""
Alrighty, so you said '{likes}' about liking me. You live in {lives}...not sure where that is. Also, you have a {computer} computer. I suppose that's where I live, nice!
""")
