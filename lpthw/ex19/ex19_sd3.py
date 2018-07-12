def our_chicken(white, black, red):
    print(f"We have {white} white chicken.")
    print(f"There are {black} black chicken in our backyard.")
    print(f"The rest {red} of them are red.")
    # I need a return for my # 3 , where I print the function. 
    # If I don't have a return, the function's value is None
    return(white + black + red)

print("1")
our_chicken(12, 5, 4) # 1

print("2")
whites = 12
blacks = 5
reds = 4
our_chicken(whites, blacks, reds) # 2

print("3")
print(our_chicken(12, 5, 4)) # 3

print("4")
our_chicken(2 * 6, 7 - 2, 1 + 3) # 4

print("5")
our_chicken(12.0, 5.0, 4.0) # 5

print("6")
white_chicken = int(input("Number of white chicken: "))
black_chicken = int(input("Number of black chicken: "))
red_chicken = int(input("Number of red chicken: "))
our_chicken(white_chicken, black_chicken, red_chicken) # 6

print("7")
our_chicken(white_chicken + 12, black_chicken + 5, red_chicken + 4) # 7

print("8")
def village_chicken():
    our_chicken(12, 5, 4)
village_chicken()

print("9")
our_chicken(23*17, 5, 4) # 9
print("10")
our_chicken(white_chicken, 5, red_chicken) # 10