##---- FUNCTIONS ----##
def greeting():
    print("Greetings, User.")


def greeting_w_name(name):
    print(f"Greetings, {name}.")

def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def divide(a, b):
    print(a / b)

def multiply(a, b):
    print(a * b)

##---- CALLING FUNCTIONS ----##
# greeting()
# greeting_w_name("Agape")
# greeting_w_name("Amiel")
# greeting_w_name("Joshua")
# add(25, 100)
# add(150, 240)
# add(0, 5)
# subtract(100, 50)
# subtract(500, 250)
# subtract(1750, 450)

operation = input("Which operation do you want to use:\n+\n-\n*\n/ \n\n>>")
a = input("Enter your first number: \n>>")
b = input("Enter your second number: \n>>")

if operation == "+":
    add(a, b)
elif operation == "-":
    subtract(a, b)
elif operation == "/":
    divide(a, b)
elif operation == "*":
    multiply(a, b)
else:
    print()
