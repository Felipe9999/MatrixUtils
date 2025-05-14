#TODO: ESTE ARCHIVO ES SOLO DE PRUEBA, NO USAR

#TODO: Temporary function, for testing only. Remove when integrating to main codebase
from GaussJordan import *
from InverseMatrix import *


def constructMatrix():
    size = int(input("Ingrese el tamaño de su matriz (cuadrada):\n"))
    rawInput = input("Ingrese los "+str(size*size)+" elementos separados por comas:\n").split(',')
    matrix: list[list] = []
    for i in range(0, size):
        matrix.append([])
        for j in range(0, size):
            matrix[i].append(int(rawInput[(size*i)+j]))
    return matrix

def test(): #TODO: Testing only, remove when combining to the other code
    #testMatrix = [[1,2,3,10], [4,5,6,11], [7,8,9,12]]
    testMatrix = [
        [16,    -6, 4,  1, -36],
        [1,     -8, 1,  1, -64],
        [16,    2,  -4, 1, -4],
        [9,     8,  -3, 1, -64],
    ]
    resultMatrix = GaussJordan(testMatrix)
    print("Reducción Gauss Jordan:", resultMatrix)
    resultVec = equationSystemSolver(testMatrix)
    print("Solución (vec o matriz):", resultVec)

def test2(): #TODO: Testing only, remove when combining to the other code
    #testMatrix = [[1,2,3,10], [4,5,6,11], [7,8,9,12]]
    testMatrix = [
        [16,    -6, 4,  1, -36, 11],
        [1,     -8, 1,  1, -64, 23],
        [16,    2,  -4, 1, -4, 43],
        [9,     8,  -3, 1, -64, 33],
    ]
    resultMatrix = GaussJordan(testMatrix)
    print("Reducción Gauss Jordan:", resultMatrix)
    resultVec = equationSystemSolver(testMatrix)
    print("Solución (vec o matriz):", resultVec)

test()
test2()
matrix = constructMatrix()
print("Determinante:" ,getDeterminant(matrix))
print("Cofactores:", getCofactors(matrix))
print("Inversa:", getInverse(matrix))
resultMatrix = GaussJordan(matrix)
print("Reducción Gauss Jordan:", resultMatrix)
resultVec = equationSystemSolver(matrix)
print("Resultado de sys de ecuaciones:", resultVec)

