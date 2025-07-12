# power_calculator.py
def main():
    try:
        base_input = input("Enter number: ")
        base = float(base_input)
    except ValueError:
        print("Invalid number input.") #숫자 입력이 숫자형 아닐 경우
        return

    try:
        exponent_input = input("Enter exponent: ")
        exponent = int(exponent_input)
    except ValueError:
        print("Invalid exponent input.")  # 지수 입력이 정수가 아닐 경우
        return

    result = 1.0
    for _ in range(abs(exponent)):
        result *= base

    if exponent < 0:
        result = 1 / result

    if result.is_integer():
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
