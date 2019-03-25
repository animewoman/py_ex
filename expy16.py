from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit ctlr-c")
print("If you do want that, hit enter")

input('?')
print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file")  # опустошает файл
print("input three lines pls")
line1 = input("line1 is:")
line2 = input("line2 is:")
line3 = input("line3 is:")

print("Now we are going to write these three lines to the file")

target.write(line1, "\n")
target.write(line2, "\n")
target.write(line3, "\n")
print("And finally, we close it.")
target.close()
