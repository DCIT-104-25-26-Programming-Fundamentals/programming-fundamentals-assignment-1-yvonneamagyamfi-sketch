def transpose_matrix(matrix):
    if not matrix:
        return []

    transposed = []
    for column in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][column])
        transposed.append(new_row)
    return transposed


def add_matrices(matrix_a, matrix_b):
    result = []
    for row in range(len(matrix_a)):
        new_row = []
        for column in range(len(matrix_a[row])):
            new_row.append(matrix_a[row][column] + matrix_b[row][column])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    if not matrix_a or not matrix_b or len(matrix_a[0]) != len(matrix_b):
        raise ValueError("The matrices cannot be multiplied.")

    result = []
    for row in range(len(matrix_a)):
        new_row = []
        for column in range(len(matrix_b[0])):
            value = 0
            for inner in range(len(matrix_b)):
                value += matrix_a[row][inner] * matrix_b[inner][column]
            new_row.append(value)
        result.append(new_row)
    return result


def read_matrix(rows, columns):
    matrix = []
    for row in range(rows):
        while True:
            values = input(f"Enter row {row + 1}: ").split()
            if len(values) == columns:
                row_values = []
                for value in values:
                    number = float(value)
                    row_values.append(int(number) if number.is_integer() else number)
                matrix.append(row_values)
                break
            print(f"Error: Enter exactly {columns} values.")
    return matrix


def display_matrix(matrix):
    if not matrix:
        print("(empty matrix)")
        return

    width = 0
    for row in matrix:
        for value in row:
            if len(str(value)) > width:
                width = len(str(value))
    for row in matrix:
        print(" ".join(f"{value:>{width}}" for value in row))


def read_dimensions(title):
    print(title)
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    return rows, columns


def main():
    rows, columns = read_dimensions("PART A - Transpose a Matrix")
    matrix = read_matrix(rows, columns)
    print("Original Matrix:")
    display_matrix(matrix)
    print("Transposed Matrix:")
    display_matrix(transpose_matrix(matrix))

    rows, columns = read_dimensions("\nPART B - Add Two Matrices")
    print("Enter the first matrix:")
    matrix_a = read_matrix(rows, columns)
    print("Enter the second matrix:")
    matrix_b = read_matrix(rows, columns)
    print("Sum:")
    display_matrix(add_matrices(matrix_a, matrix_b))

    rows_a, columns_a = read_dimensions("\nPART C - Multiply Two Matrices")
    print("Enter matrix A:")
    matrix_a = read_matrix(rows_a, columns_a)
    rows_b, columns_b = read_dimensions("Enter the dimensions for matrix B")
    if columns_a != rows_b:
        print("Error: The columns in matrix A must equal the rows in matrix B.")
        return
    print("Enter matrix B:")
    matrix_b = read_matrix(rows_b, columns_b)
    print("Product:")
    display_matrix(multiply_matrices(matrix_a, matrix_b))


if __name__ == "__main__":
    main()
