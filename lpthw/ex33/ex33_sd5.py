def range_func(incr, up_limit):
    numbers = []
    numbers = range(incr, up_limit)
    for number in numbers:
        print(f"The number is {number}")
        
    print("The numbers: ")
    for number in numbers:
        print(number)

range_func(1, 6)