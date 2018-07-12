# sets formatter to {} {} {} {}
formatter = "{} {} {} {}"

# calls format() method on formatter variable and gives 4 arguments to replace the {}'s. Prints the result
print(formatter.format(1, 2, 3, 4))
# gives 4 strings as arguments to replace the {}'s in the formatter. Prints all
print(formatter.format("one", "two", "three", "four"))
# gives True and False as arguments to replace the {} in formatter. Prints the result
print(formatter.format(True, False, False, True))
# gives variable formatter as argument to replace the 4 {}'s. Prints it all
print(formatter.format(formatter, formatter, formatter, formatter))
# gives strings as arguments to replace the {}'s in formatter. Prints all
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))