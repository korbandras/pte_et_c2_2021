def hello():
    name=input("What's your name?\n")
    print(f"Hi {name}!")
def greetings(name):
    if type(name)==str:
        print(f"Hi {name}!")
hello()
greetings(input(("What's your name?\n")))