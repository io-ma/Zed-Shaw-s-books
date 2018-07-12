# sets types_of_people to 10
types_of_people = 10
# sets x to a string containing types_of_people variable
x = f"There are {types_of_people} types of people."

# sets binary to "binary"
binary = "binary"
# sets do_not tp "don't"
do_not = "don't"
# sets y to a string that contains binary and do_not variables
y = f"Those who know {binary} and those who {do_not}."

# prints the x variable
print(x)
# prints the y variable
print(y)

# prints a string that contains the x variable
print(f"I said: {x}")
# prints a string that contains the y variable
print(f"I also said: '{y}'")

# sets hilarious to False
hilarious = False
# sets joke_evaluation to a string that contains the {} 
joke_evaluation = "Isn't that joke so funny?! {}"

# prints joke_evaluation and formats the hilarious variable to string
print(joke_evaluation.format(hilarious))

# sets w to a string
w = "This is the left side of..."
# sets e to a string
e = "a string with a right side."

# concatenates w and e and prints them
print(w + e)