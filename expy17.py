from sys import argv
from os.path import exists

scripts, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
in_data = in_file.read()
print(f"input files is {len(in_data)} bytes long")
print(f"Doest the output file exists ? {exists(to_file)}")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)
print("We did it")
out_file.close() # почему мы должны закрывать файл? потому, что питон может сам не закрыт файл, это затормозит работу пк и большинство изменений вступают только тогда, когда закрывают файл
in_file.close()
