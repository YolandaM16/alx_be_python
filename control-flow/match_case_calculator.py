num1 = float(input("Enter the number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 ! = 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    casew _:
        print("Invalid operation. Please choose from +, -, *, or /.")
