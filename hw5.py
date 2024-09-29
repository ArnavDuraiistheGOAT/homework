def sum_diagonal(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))
matrix = [list(map(int, row.split(','))) for row in input().split()]
print("Sum of the diagonal is:", sum_diagonal(matrix))
