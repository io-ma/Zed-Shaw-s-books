from sys import argv

def main():
    args = argv
    i = 0
    for arg in args:
        print(f"arg {i}: {arg}")
        i += 1

    states = ["California", "Oregon", "Washington", "Texas"]
    j = 0
    for state in states:
        print(f"state {j}: {state}")
        j += 1

main()

