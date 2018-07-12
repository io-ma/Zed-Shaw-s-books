def loop(bigger_number):
    i = 0
    numbers = []
    while i < bigger_number:
        numbers.append(i)
        i = i + 1

    print("The numbers: ")
    for num in numbers:
        print(num)

loop(6)