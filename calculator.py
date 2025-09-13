
# first_name = input("What is your first name?")
# last_name = input("What is your last name?")

# def format_name(f_name, l_name):
#     if f_name and l_name is not None:
#         output = f_name + " " + l_name
#         print(output.title())
#         return output.title()
#     else:
#         print("Invalid: Please provide a first name and last name.")
      
# format_name(f_name=first_name, l_name=last_name)

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

# Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

print(operations["*"](4, 8))

# Functionality
# • Program asks the user to type the first number.

first_num = int(input("Type in the first number:"))

while True:

    # • Program asks the user to type a mathematical operator (e.g. "+", "-", "*" or "/").
    math_op = input(f"Please type in a mathematical operation: {' '.join(operations)} ")
    # • Program asks the user to type the second number.
    sec_num = int(input("Type in the second number:"))
    # • Program works out the result based on the chosen mathematical operator.
    result = operations[math_op](first_num, sec_num)
    print(result)
    # • Program asks if the user wants to continue working with the previous result.
    res = input('Would you like to continue working with the previous result? (Y/n) or "Exit"')
    if res.lower() == "n":
        # • If no, program asks the user for the first number to start the calculation process from the beginning.
        first_num = int(input("Type in the first number:"))
    elif res.lower() == "exit":
        break
    else:
        # • If yes, program loops to use the previous result as the first number and then repeats the calculation process.
        first_num = result
