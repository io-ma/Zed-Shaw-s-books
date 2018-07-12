# cars is 100
cars = 100
# space_in_a_car is 4.0
space_in_a_car = 4.0
# drivers is 30
drivers = 30
# passengers is 90
passengers = 90
# cars_not_driven is cars - drivers
cars_not_driven = cars - drivers
# cars_driven is drivers
cars_driven = drivers
# carpool_capacity is cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car is passengers / cars_driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, 
      "in each car.")