def display_menu():
    print("\nMenu:")
    print("1. Matrix Addition")
    print("2. Matrix Multiplication")
    print("3. Matrix Transpose")
    print("4. Exit")

def input_matrix(rows, cols):
    matrix = []
    print(f"Enter elements for {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} values separated by spaces: ").split()))
        matrix.append(row)
    return matrix

def matrix_addition(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

def matrix_multiplication(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    return result

def matrix_transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return result

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1": 
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print("Enter the first matrix:")
        matrix1 = input_matrix(rows, cols)
        print("Enter the second matrix:")
        matrix2 = input_matrix(rows, cols)
        print("Resultant Matrix after Addition:")
        result = matrix_addition(matrix1, matrix2)
        display_matrix(result)

    elif choice == "2":  
        rows1 = int(input("Enter the number of rows for the first matrix: "))
        cols1 = int(input("Enter the number of columns for the first matrix: "))
        matrix1 = input_matrix(rows1, cols1)

        rows2 = int(input("Enter the number of rows for the second matrix: "))
        cols2 = int(input("Enter the number of columns for the second matrix: "))

        if cols1 != rows2:
            print("Matrix multiplication is not possible! Number of columns of the first matrix must equal the number of rows of the second matrix.")
        else:
            matrix2 = input_matrix(rows2, cols2)
            print("Resultant Matrix after Multiplication:")
            result = matrix_multiplication(matrix1, matrix2)
            display_matrix(result)

    elif choice == "3":  
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        matrix = input_matrix(rows, cols)
        print("Transpose of the Matrix:")
        result = matrix_transpose(matrix)
        display_matrix(result)

    elif choice == "4": 
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
