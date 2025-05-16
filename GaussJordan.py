#Realiza una operación entre dos filas de una matriz.
def RowOperation(R1: list, R2: list, multiplier1, multiplier2):
    NewR2 = R2
    if(multiplier1 != 0 and multiplier2 != 0): #check that the operation is valid
        for i in range (0, len(R1)): #int i = 0; i < R1.length; i++
            NewR2[i] = multiplier2*R1[i]+multiplier1*R2[i]
        return NewR2
    else: return None

#Aplica la eliminación gaussiana a una matriz.
def Gauss(Matrix: list[list]):
    newMatrix = Matrix
    matrixLen = len(Matrix[0])
    for i in range(0, len(Matrix)): #(int i = 0; i < Matrix.length; i++)
        #for j in range(i+1, matrixLen): #(int j = i+1; j < matrixLen-1; j++)
        #    newMatrix[j] = RowOperation(Matrix[i], Matrix[j], -Matrix[i][i], Matrix[j][i])
        j = i+1
        pivot = 0
        while(pivot < matrixLen and Matrix[i][pivot] == 0): pivot+=1 #move the pivot to where it belongs
        if(pivot == matrixLen): pivot-=1
        while (j < matrixLen and j < len(newMatrix)):
            row = RowOperation(Matrix[i], Matrix[j], -Matrix[i][pivot], Matrix[j][pivot])
            if(not row is None): newMatrix[j] = row
            else: newMatrix[j] = Matrix[j]
            j+=1
    return RowsOfZeroToBottom(newMatrix)

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
        pivot = 0
        while(pivot < matrixLen and Matrix[i][pivot] == 0): pivot+=1 #move the pivot to where it belongs
        if(pivot == matrixLen): pivot-=1
        currentVal = newMatrix[i][pivot]
        if(currentVal != 0):
            operator = 1/newMatrix[i][pivot]
            if(operator != 0):
                SingleRowOperationFloat(newMatrix[i], operator)
                for j in range(i-1, -1, -1): #(int j = i-1; j >= 0; j--)
                    row = RowOperation(newMatrix[i], newMatrix[j], -newMatrix[i][pivot], newMatrix[j][pivot])
                    if(not row is None): newMatrix[j] = row
                    else: newMatrix[j] = Matrix[j]
    return RowsOfZeroToBottom(newMatrix)

#Crea una matriz en la que todas las filas de cero quedan abajo
def RowsOfZeroToBottom(matrix: list[list]):
    columnLen = len(matrix[0])
    length = len(matrix)
    newMat = removeRowsOfZero(matrix)
    newLen = len(newMat)
    for i in range(newLen, length):
        newMat.append([])
        for j in range(0, columnLen):
            newMat[i].append(0)
    return newMat

#Aplica Gauss seguido de Jordan a una matriz, para reducción Gauss-Jordan completa.
def GaussJordan(Matrix: list[list]): return Jordan(Gauss(Matrix))

#Elimina las filas que son completamente ceros de una matriz.
def removeRowsOfZero(Matrix: list[list]):
    length = len(Matrix[0])
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
    length = len(reducedEqMatrix[0])
    hasSln = True
    i = 0
    #for i in range(0, len(reducedEqMatrix)):
    while(i < len(reducedEqMatrix) and hasSln):
        j = 0
        isZeroRow = True
        while(j < length-1 and isZeroRow):
            if(reducedEqMatrix[i][j] != 0): isZeroRow = False
            j+=1
        if(isZeroRow and reducedEqMatrix[i][length-1] != 0):
            hasSln = False
        i+=1
    return hasSln

#Resuelve un sistema de ecuaciones lineales.
def equationSystemSolver(eqAsMatrix: list[list]):
    resultMat = removeRowsOfZero(Jordan(removeRowsOfZero(Gauss(eqAsMatrix))))
    length = len(resultMat[0])
    resultVec = []
    if(hasSolution(resultMat)):
        if(length-len(resultMat) == 1):
            for i in range(0, len(resultMat)):
                resultVec.append(resultMat[i][length-1])
            return resultVec
        else:
            #for i in range(0, len(resultMat)):
            #    resultVec.append([])
            #    for j in range(len(resultMat), length):
            #        resultVec[i].append(resultMat[i][j])
            #return resultVec
            #return equationSysMultiVar(resultMat)
            print("El sistema tiene soluciones infinitas.")
            return resultMat
    else: return "El sistema no tiene solución"

