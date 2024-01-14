def spiral_matrix(size: int) -> list[list[int]]:
    matrix: list[list[int]] = [[0] * size for i in range(size)]
    numbers: list[int] = [i for i in range(1, size * size + 1)]
    
    for i in range(size // 2):
        for j in range(i, size - i):
            matrix[i][j] = numbers.pop(0)
        for j in range(1 + i, size - 1 - i):
            matrix[j][-1 - i] = numbers.pop(0)
        for j in range(size - 1 - i, i - 1, -1):
            matrix[size - 1 - i][j] = numbers.pop(0)
        for j in range(size - 2 - i, i, -1):
            matrix[j][i] = numbers.pop(0)
    if size % 2 == 1:
        matrix[size // 2][size // 2] = numbers.pop(0)
    return matrix

    
for row in spiral_matrix(7):
        print(f"{' '.join([str(elem).ljust(2) for elem in row])}")
