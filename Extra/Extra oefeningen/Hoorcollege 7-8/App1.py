original_matrix = [[1, 2, 3, 4],
                   [1, 2, 3, 4],
                   [1, 2, 3, 4]]

transposed_matrix = []
for i in range(len(original_matrix[0])):
    new_row = []
    for j in range(len(original_matrix)):
        new_row.append(original_matrix[j][i])
    transposed_matrix.append(new_row)

print(*transposed_matrix, sep="\n")