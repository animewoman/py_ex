from sys import argv
script, user_name = argv

prompt = '> '
print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you question")
print("Where you do live?")
lives = input(prompt)
print(f"Okay. So you live in {lives}")
