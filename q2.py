def is_toeplitz_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
# Check the diagonal from top-left to bottom-right
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True


# Read the dimensions of the matrix
rows, cols = map(int, input().split())

# Read the matrix elements
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Check if the matrix is Toeplitz
if is_toeplitz_matrix(matrix):
    print("Identical")
else:
    print("Not Identical")