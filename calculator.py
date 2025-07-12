def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

if __name__ == "__main__":
    try:
        num1 = int(float(input("Enter first number: ")))
        num2 = int(float(input("Enter second number: ")))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operator."

        print(f"Result: <{result}>")
    except ValueError:
        print("Invalid operator.")
