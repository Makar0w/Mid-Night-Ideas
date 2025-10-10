import zlib
user_input = input("File Name -->")
file = open(user_input, "r")
data = file.read()
comp = zlib.compress(bytes(data, 'utf-8'))
with open("Compressed.txt", "wb") as file:
    file.write(comp)