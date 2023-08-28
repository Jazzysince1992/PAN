# Creating a 2D array (3x3 matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element at row 1, column 2 (remember, 0-based indexing)
element = matrix[1][2]  # This would be 6 in the example matrix

# Iterating through the matrix
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Move to the next row

# Modifying an element
matrix[0][1] = 10  # Changing the element at row 0, column 1 to 10

# Finding the dimensions of the matrix
num_rows = len(matrix)
num_cols = len(matrix[0]) if num_rows > 0 else 0


