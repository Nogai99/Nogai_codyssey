# calculator.py

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
    while True:
        print("Select input method:")
        print("1. 실수형 숫자 2개와 연산자 하나를 각각 입력")
        print('2. 사용자 입력 형식: "숫자 연산자 숫자" 형태 (공백 포함)')

        choice = input("Enter 1 or 2: ")

        try:
            if choice == "1":
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
                    print("Error: Invalid operator. Allowed: +, -, *, /")
                    continue

                print(f"Result: <{result}>")
                break

            elif choice == "2":
                expr = input("Enter expression: ")
                parts = expr.strip().split()

                if len(parts) != 3:
                    print("Error: Invalid expression format. Use space between number, operator, and number.\n")
                    continue

                a_str, op, b_str = parts

                # 연산자 유효성 검사
                if op not in ["+", "-", "*", "/"]:
                    print("Error: Invalid operator. Allowed: +, -, *, /")
                    continue

                # 연산자가 여러 개 포함되었는지 검사
                op_count = sum(1 for c in expr if c in "+-*/")
                if op_count > 1:
                    print("Error: Only one operator is allowed.\n")
                    continue

                a = int(float(a_str))
                b = int(float(b_str))

                if op == "+":
                    result = add(a, b)
                elif op == "-":
                    result = subtract(a, b)
                elif op == "*":
                    result = multiply(a, b)
                elif op == "/":
                    result = divide(a, b)

                print(f"Result: <{result}>")
                break

            else:
                print("Error: Invalid selection. Please enter 1 or 2.\n")

        except ValueError:
            print("Error: Please enter valid numbers.\n")
