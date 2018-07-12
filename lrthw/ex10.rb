tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."
unicode = "\u0048\u0065\u006C\u006C\u006F World"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
quotes = '''
Let\'s see what this does.
It actually looks weird.
The puts is not highlighted as it should...
so I am using a #{tabby_cat}
See what happens.
'''


puts tabby_cat
puts persian_cat
puts backslash_cat
puts fat_cat
puts unicode
puts quotes