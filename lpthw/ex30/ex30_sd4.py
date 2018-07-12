# assigns 30 to people
people = 30
# assigns 40 to cars
cars = 40
# assigns 15 to trucks
trucks = 15

# checks if cars > people is True
if cars > people:
    # if cars > people is True, this print is executed
    print("We should take the cars.")

# checks if cars < people is True
elif cars < people:
    # if cars < people is True, this print is executed
    print("We should not take the cars.")

# if all the above are False, cars == people is True
else:
    # this print is executed
    print("We can't decide.")

# checks if trucks > cars is True
if trucks > cars:
    # if trucks > cars is True, this print is executed
    print("That's too many trucks.")

# checks if trucks < cars is True
elif trucks < cars:
    # if trucks < cars is True, this print is executed
    print("Maybe we could take the trucks.")

# if trucks > cars and trucks < cars are False, trucks == cars is True
else:
    # this print is executed
    print("We still can't decide.")

# checks if people > trucks is True
if people > trucks:
    # if people > trucks is True, this print is executed
    print("Alright, let's just take the trucks.")
# in all other cases people < trucks or people == trucks
else:
    # this print is executed
    print("Fine, let's stay home then.")