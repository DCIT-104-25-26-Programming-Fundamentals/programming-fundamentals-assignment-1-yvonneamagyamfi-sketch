def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ValueError("Cannot divide by zero.")
    return round(first / second, 2)


def modulus(first, second):
    if second == 0:
        raise ValueError("Cannot divide by zero.")
    return first % second


def exponentiate(first, second):
    return first ** second


def calculate_result(choice, first, second):
    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide,
        "5": modulus,
        "6": exponentiate,
    }
    return operations[choice](first, second)


def format_number(number):
    if isinstance(number, float) and number.is_integer():
        return str(int(number))
    return str(number)


def print_menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        print_menu()
        choice = input("Select an operation (1-7): ").strip()
        if choice == "7":
            print("Goodbye!")
            break
        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Error: Please choose a number from 1 to 7.")
            continue

        try:
            first = float(input("Enter first number : "))
            second = float(input("Enter second number: "))
            result = calculate_result(choice, first, second)
            print(
                f"Result: {format_number(first)} { {'1': '+', '2': '-', '3': '*', '4': '/', '5': '%', '6': '**'}[choice] } "
                f"{format_number(second)} = {format_number(result)}"
            )
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
