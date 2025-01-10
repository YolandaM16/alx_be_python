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
