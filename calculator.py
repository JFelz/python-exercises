
first_name = input("What is your first name?")
last_name = input("What is your last name?")

def format_name(f_name, l_name):
    if f_name and l_name is not None:
        output = f_name + " " + l_name
        print(output.title())
        return output.title()
    else:
        print("Invalid: Please provide a first name and last name.")
      
format_name(f_name=first_name, l_name=last_name)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(operations["*"](4, 8))

first_num = int(input("Type in the first number:"))

while True:
    math_op = input(f"Please type in a mathematical operation: {' '.join(operations)} ")
    sec_num = int(input("Type in the second number:"))
    result = operations[math_op](first_num, sec_num)
    print(result)
    res = input('Would you like to continue working with the previous result? (Y/n) or "Exit"')
    if res.lower() == "n":
        first_num = int(input("Type in the first number:"))
    elif res.lower() == "exit":
        break
    else:
        first_num = result
