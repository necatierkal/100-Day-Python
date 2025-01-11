

import art


def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    print(art.logo)
    should_accumulate = True
    n1 = float(input("What's the first number?: "))
    while should_accumulate:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        n2= float(input("What's the next number?: "))
        answer = operations[operation_symbol](n1,n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:  ")
        if choice == 'y':
            n1 = answer
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()

calculator()

#
# devammi=True
# process = 0
# while devammi:
#     n1= float(input("What's the first number?: "))
#     operator = input("""
#     +
#     -
#     *
#     /
#     Pick an opartion: """)
#
#     n2= float(input("What's the next number?: "))
#
#     if operator == "+":
#         process=add(n1,n2)
#         print(f"{n1} + {n2} = {process}\n")
#     elif operator == "-":
#         process=subtract(n1,n2)
#         print(f"{n1} - {n2} = {process}\n")
#     elif operator == "*":
#         process=multiply(n1,n2)
#         print(f"{n1} * {n2} = {process}\n")
#     elif operator == "/":
#         process=divide(n1,n2)
#         print(f"{n1} / {n2} = {process}\n")
#
#
#     devammi_string = input(f"Type 'y' to continue calculating with {process}, or type 'n' to start a new calculation:  ")
#     if devammi_string == 'y':
#         devammi = True
#     elif devammi_string == 'n':
#         devammi = False

