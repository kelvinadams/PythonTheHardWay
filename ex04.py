# Python the Hard Way - Exercise 4

# assigning variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

# printing the output for carpooling information, mixing text and declared variables into the output
print("There are", cars, "cars available.")
# notice you don't need a space at the end of each "" for their to be a space in the sentence like in Excel when concatenating strings and cell values
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need about", average_passengers_per_car, "in each car.")
