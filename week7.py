# Goal:


from click import prompt


def _introduction(operation):
    welcome_string = "Welcome to calculator program. "
    prompt_string = f"Please give me two values to {operation}"
    print(f"{welcome_string}\n{prompt_string}")

def _get_number(i):
    number = float(input(f"Number {i}: "))
    return number


def _print_result(first_number, second_number, operation, result):
    print(f"{first_number} {operation} {second_number} = {result}")

#---------------#

def add_numbers():
    _introduction("add")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1+num2
    _print_result(num1, num2, "+", result)

def subtract_numbers():
    _introduction("subtract")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1-num2
    _print_result(num1, num2, "-", result)

def multiply_numbers():
    _introduction("multiply")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1*num2
    _print_result(num1, num2, "*", result)

def divide_numbers():
    _introduction("divide")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1/num2
    _print_result(num1, num2, "/", result)

