def print_table(number):
    print(f"Multiplication Table for {number}:")
    for multiplier in range(1, 13):
        print(f"{number}  x  {multiplier:2}  =  {number * multiplier}")


def print_tables_up_to(limit):
    for number in range(1, limit + 1):
        print_table(number)
        if number != limit:
            print("---------------------------")


def main():
    number = int(input("Enter a number for the single table: "))
    print_table(number)

    limit = int(input("Enter N for tables from 1 to N: "))
    if limit <= 0:
        print("Error: N must be a positive integer.")
        return
    print_tables_up_to(limit)


if __name__ == "__main__":
    main()
