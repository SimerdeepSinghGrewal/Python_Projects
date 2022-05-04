# Calculator
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number ?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number ?: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        move = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to exit or type 's' to start with new calculation.: ")

        if move == "y":
            num1 = answer
        elif move == "n":
            should_continue = False
        elif move == "s":
            calculator()


calculator()