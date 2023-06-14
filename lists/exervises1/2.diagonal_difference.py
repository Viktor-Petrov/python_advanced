size = int(input())

matrix = []
first_diag = []
second_diag = []

for row in range(size):
    col = [int(n) for n in input().split()]
    matrix.append(col)

    first_diag.append(matrix[row][row])

    second_col = col[::-1]
    second_diag.append(second_col[row])

print(abs(sum(first_diag) - sum(second_diag)))
