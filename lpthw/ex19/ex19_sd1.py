# define a function called cheese_and_crackers that takes
# cheese_count and boxes_of_crackers as arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints a string that has cheese_count in it
    print(f"You have {cheese_count} cheeses!")
    # prints a string that has boxes_of_crackers in it
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # prints a string 
    print("Man that's enough for a party!")
    # prints a string and a newline
    print("Get a blanket.\n")

# prints we can give the function numbers directly
print("We can just give the function numbers directly:")
# gives cheese_and_crackers function 20 and 30 as arguments and calls it
cheese_and_crackers(20, 30)

# prints we can use variables as arguments
print("OR, we can use variables from our script:")
# assigns 10 to a variable amount_of_cheese
amount_of_cheese = 10
# assigns 50 to a variable amount_of_crackers
amount_of_crackers = 50

# calls cheese_and_crackers function with variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints we can have math inside too
print("We can even do math inside too:")
# calls cheese_and_crackers giving it math as arguments
cheese_and_crackers(10 + 20, 5 + 6)

# prints we can combine variables and math
print("And we can combine the two, variables and math:")
# calls cheese_and_crackers with variables and math as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)