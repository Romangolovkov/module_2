def rating_workplaces(size: int) -> list[list[int]]:
    matrix: list[list[int]] = [[9] * size for i in range(size)]

    for i in range(size):
        matrix[i][size - 1 - i] = 5
        matrix[i][i] = 0
        for j in range(size):
            if i < j:
                if (i + j) < (size - 1):
                    matrix[i][j] = 1
                elif (i + j) > (size - 1):
                    matrix[i][j] = 4                
            if i > j:
                if (i + j) < (size - 1):
                    matrix[i][j] = 2
                elif (i + j) > (size - 1):
                    matrix[i][j] = 3
            
    return matrix    
 

for row in rating_workplaces(7):
        print(' '.join([str(elem) for elem in row]))