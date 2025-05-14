#Calcula el determinante de una matriz cuadrada.
def getDeterminant(matrix: list[list]):
    determinant = 0
    if (len(matrix) == len(matrix[0])):
        length = len(matrix)
        if(length == 1): determinant = matrix[0][0]
        elif (length == 2):
            determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            for i in range(0, length):
                newMatrix: list[list] = []
                for j in range(0, (length-1)): #rows
                    newMatrix.append([])
                    for k in range(0, (length-1)): #cols
                        if (k < i):
                            newMatrix[j].append(matrix[j+1][k])
                        else: newMatrix[j].append(matrix[j+1][k+1])
                partialDet = getDeterminant(newMatrix)
                if (i % 2 == 0):
                    determinant += matrix[0][i] * partialDet
                else:
                    determinant -= matrix[0][i] * partialDet
    else:
        print("La matriz no es cuadrada!")
    return determinant

#Elimina una fila y una columna específica de una matriz.
def removeRowColAt(matrix: list[list], row, col):
    newMatrix: list[list] = []
    for i in range(0, len(matrix)-1):
        if(i < row): currentRow = i
        else: currentRow = i+1
        newMatrix.append([])
        for j in range(0, len(matrix[0])-1):
            if(j < col): currentCol = j
            else: currentCol = j+1
            newMatrix[i].append(matrix[currentRow][currentCol])
    return newMatrix

#Calcula la matriz de cofactores.
def getCofactors(matrix: list[list]):
    cofactors: list[list] = []
    if (len(matrix) == len(matrix[0])):
        length = len(matrix)
        for i in range(0, length): #rows
            cofactors.append([])
            for j in range(0, length): #cols
                newMatrix = removeRowColAt(matrix ,i, j)
                currentCof = getDeterminant(newMatrix)
                if ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
                    cofactors[i].append(currentCof)
                else:
                    cofactors[i].append(-currentCof)
    else:
        print("La matriz no es cuadrada!")
    return cofactors

#Multiplica todos los elementos de una matriz por un número.
def multiplyMatrixByNumber(number, matrix: list[list]):
    result: list[list] = []
    for i in range(0, len(matrix)):
        result.append([])
        for j in range(0, len(matrix[0])):
            result[i].append(number * matrix[i][j])
    return result

#Calcula la transpuesta de una matriz.
def transpose(matrix: list[list]):
    transposed: list[list] = []
    for i in range(0, len(matrix[0])):
        transposed.append([])
        for j in range(0, len(matrix)):
            transposed[i].append(matrix[j][i])
    return transposed

#Calcula la inversa de una matriz cuadrada.
def getInverse(matrix: list[list]):
    determinant = getDeterminant(matrix)
    if(determinant != 0):
        if(len(matrix) > 1 and len(matrix[0]) > 1):
            adjugate = transpose(getCofactors(matrix))
            return multiplyMatrixByNumber((1/determinant), adjugate)
        else: return [[1/matrix[0][0]]] #the inverse of a single element matrix is itself
    else: return "La matriz es singular."