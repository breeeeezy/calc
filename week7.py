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

def calculate(operation):
    _introduction(operation)
    num1 = _get_number(1)
    num2 = _get_number(2)

    if operation == "add":
        result = num1+num2
    if operation == "subtract":
        result = num1-num2
    if operation == "multiply":
        result = num1*num2
    if operation == "divide":
        result = num1/num2

    _print_result(num1, num2, operation, result)
#---------------#
