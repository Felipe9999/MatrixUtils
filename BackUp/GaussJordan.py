#Realiza una operación entre dos filas (combinación lineal).
def RowOperation(R1: list, R2: list, multiplier1, multiplier2):
    for i in range (0, len(R1)): #int i = 0; i < R1.length; i++
        R2[i] = multiplier2*R1[i]+multiplier1*R2[i]
    return R2

#Aplica la eliminación gaussiana a una matriz.
def Gauss(Matrix: list[list]):
    newMatrix = Matrix
    matrixLen = len(Matrix[0])
    for i in range(0, len(Matrix)): #(int i = 0; i < Matrix.length; i++)
        #for j in range(i+1, matrixLen): #(int j = i+1; j < matrixLen-1; j++)
        #    newMatrix[j] = RowOperation(Matrix[i], Matrix[j], -Matrix[i][i], Matrix[j][i])
        j = i+1
        while (j < matrixLen and j < len(newMatrix)):
            newMatrix[j] = RowOperation(Matrix[i], Matrix[j], -Matrix[i][i], Matrix[j][i])
            j+=1
    return newMatrix;

#Multiplica una fila por un número de tipo floating point.
def SingleRowOperationFloat(R1: list, multiplier):
    newR1 = R1
    for i in range(0, len(R1)): #(int i = 0; i < R1.length; i++)
        newR1[i] = R1[i]*multiplier
    return R1

#Aplica la eliminación de Jordan (reducción gaussiana total) a una matriz de forma Gauss
def Jordan(Matrix: list[list]):
    newMatrix = Matrix
    matrixLen = len(newMatrix[0])
    for i in range(len(newMatrix)-1, -1, -1): #(int i = newMatrix.length-1; i >= 0; i--)
        currentVal = newMatrix[i][i]
        if(currentVal != 0):
            operator = 1/newMatrix[i][i]
            if(operator != 0):
                SingleRowOperationFloat(newMatrix[i], operator)
                for j in range(i-1, -1, -1): #(int j = i-1; j >= 0; j--)
                    newMatrix[j] = RowOperation(newMatrix[i], newMatrix[j], -newMatrix[i][i], newMatrix[j][i]);
    return newMatrix

#Aplica Gauss seguido de Jordan a una matriz.
def GaussJordan(Matrix: list[list]): return Jordan(Gauss(Matrix))

#Elimina las filas que son completamente ceros de una matriz.
def removeRowsOfZero(Matrix: list[list]):
    length = len(Matrix)
    resultMatrix: list[list] = []
    for i in range(0, len(Matrix)):
        j = 0
        keepRow = False
        while(j < length and not keepRow):
            if(Matrix[i][j] != 0): keepRow = True
            j+=1
        if(keepRow): resultMatrix.append(Matrix[i])
    return resultMatrix

#Verifica si un sistema de ecuaciones tiene solución.
def hasSolution(reducedEqMatrix: list[list]):
    length = len(reducedEqMatrix)
    hasSln = True
    i = 0
    #for i in range(0, len(reducedEqMatrix)):
    while(i < len(reducedEqMatrix) and hasSln):
        j = 0
        isZeroRow = True
        while(j < length-1 and not isZeroRow):
            if(reducedEqMatrix[i][j] != 0): isZeroRow = False
            j+=1
        if(not isZeroRow and reducedEqMatrix[i][length-1] == 0):
            hasSln = False
        i+=1
    return hasSln

#Resuelve un sistema de ecuaciones lineales.
def equationSystemSolver(eqAsMatrix: list[list]):
    resultMat = removeRowsOfZero(Jordan(removeRowsOfZero(Gauss(eqAsMatrix))))
    length = len(resultMat[0])
    resultVec = []
    if(length-len(resultMat) == 1):
        for i in range(0, len(resultMat)):
            resultVec.append(resultMat[i][length-1])
        return resultVec
    elif(length-len(resultMat) > 0):
        #for i in range(0, len(resultMat)):
        #    resultVec.append([])
        #    for j in range(len(resultMat), length):
        #        resultVec[i].append(resultMat[i][j])
        #return resultVec
        #return equationSysMultiVar(resultMat)
        return resultMat
    else: return "La matriz no es un sistema de ecuaciones válido"

