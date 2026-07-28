def generate_fibonacci(terms):
    sequence = []
    first, second = 0, 1
    for _ in range(terms):
        sequence.append(first)
        first, second = second, first + second
    return sequence


def is_fibonacci(number):
    if number < 0:
        return False

    first, second = 0, 1
    while first < number:
        first, second = second, first + second
    return first == number


def main():
    terms = int(input("How many terms? "))
    if terms <= 0:
        print("Error: Number of terms must be positive.")
        return

    print("Fibonacci sequence:", " ".join(map(str, generate_fibonacci(terms))))

    number = int(input("Enter a number to check: "))
    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()
