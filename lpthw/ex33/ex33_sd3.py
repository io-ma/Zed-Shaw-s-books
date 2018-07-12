def loop(bigger_number, incr):
    i = 0
    numbers = []
    while i < bigger_number:
        numbers.append(i)
        i = i + incr

    print("The numbers: ")
    for num in numbers:
        print(num)

loop(6, 1)