def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def calculator():
    print("Simple Calculator")

    while True:
        print("\nChoose an operation:")
        print("1. Add Two Numbers")
        print("2. Minus Two Numbers")
        print("3. Multiple Two Numbers")
        print("4. Divide Two Numbers")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1-5.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)
        print("Result:", result)

calculator()
