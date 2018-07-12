from sys import argv
script, filename = argv
text = open(filename)
print("Now we read the file", filename)
print("Bad poetry alert!")
print(text.read())
text.close()
