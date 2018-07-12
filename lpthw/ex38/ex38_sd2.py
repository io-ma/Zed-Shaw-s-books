ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# call split on ten_things; call split with the argument ten_things
# ten_things.split(' ') is split(ten_things, ' ')
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # call pop on more_stuff; call pop with the argument more_stuff
    # more_stuff.pop() is pop(more_stuff)
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # call append on stuff with the argument(next_one); call append with the arguments stuff, next_one
    # stuff.append(next_one) is append(stuff, next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
# call pop with the argument stuff
# pop(stuff)
print(stuff.pop())
# call join with the arguments stuff and ' '
# join(stuff, ' ')
print(' '.join(stuff)) # what? cool!
# call join with the arguments stuff[3:5] and '#'
# join(stuff[3:5], '#')
print('#'.join(stuff[3:5])) # super stellar!