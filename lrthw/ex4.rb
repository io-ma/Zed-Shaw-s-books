# cars takes 100
cars = 100
# space_in_a_car takes 4
space_in_a_car = 4
# drivers takes 30
drivers = 30
# passengers takes 90
passengers = 90
# cars_not_driven takes cars - drivers
cars_not_driven = cars - drivers
# cars_driven takes drivers
cars_driven = drivers
# carpool_capacity takes cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car takes passengers / cars_driven
average_passengers_per_car = passengers / cars_driven


puts "There are #{cars} cars available."
puts "There are only #{drivers} drivers available."
puts "There will be #{cars_not_driven} empty cars today."
puts "We can transport #{carpool_capacity} people today."
puts "We have #{passengers} to carpool today."
puts "We need to put about #{average_passengers_per_car} in each car."