print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world 
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")



five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# function secret_formula takes started as argument
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# start_point is assigned 10000
start_point = 10000
# beans, jars and crates are assigned the returned variables in secret_formula
# start_point is the argument
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
# formula is assigned the value returned from secret_formula(start_point)
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))