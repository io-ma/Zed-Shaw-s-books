def loop(bigger_number, incr):
    i = 0
    numbers = []
    while i < bigger_number:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += incr
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")
    for num in numbers:
        print(num)

x = int(input("first nr: "))
y = int(input("second nr: "))

loop(x, y)