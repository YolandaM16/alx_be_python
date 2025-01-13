<<<<<<< HEAD
def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message for invalid inputs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
=======
def peform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations.

    Parameters:
    - num1: First number (float)
    - num2: Second number (float)
    - operation: Operation to perform (string - 'add', 'subtract', multiply', 'divide')

    Returns:
    -The result of the operation or an error message.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Divivsion by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
>>>>>>> d4f1100964802a946b540bb6f3779179977e202b
