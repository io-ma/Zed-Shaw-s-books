people = 30
cars = 40
trucks = 15


if cars > people or people == trucks:
    print("We should take the cars.")
elif cars < people or trucks > people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars and people < cars:
    print("That's too many trucks.")
elif trucks < cars or trucks > people:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks or cars < trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")