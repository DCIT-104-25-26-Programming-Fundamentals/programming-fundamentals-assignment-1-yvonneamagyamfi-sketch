def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def calculate_average(numbers):
    if not numbers:
        return 0
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


def find_minimum(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest


def main():
    count = int(input("How many numbers? "))
    if count <= 0:
        print("Error: Number of values must be positive.")
        return

    numbers = []
    for index in range(count):
        numbers.append(float(input(f"Enter number {index + 1}: ")))

    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers):g}")
    print(f"Average: {calculate_average(numbers):g}")
    print(f"Maximum: {find_maximum(numbers):g}")
    print(f"Minimum: {find_minimum(numbers):g}")


if __name__ == "__main__":
    main()
