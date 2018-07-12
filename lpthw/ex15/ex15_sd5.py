print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())