from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)  # переходит на указанный байт


def print_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("Printing whole file")
print(current_file.read())

rewind(current_file)
print("Printing line by line")

current_line = 1
print_line(current_line, current_file)
current_line += 1
print_line(current_line, current_file)
current_line += 1
print_line(current_line, current_file)

current_file.close()
