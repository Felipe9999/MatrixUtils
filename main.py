from GaussJordan import equationSystemSolver

def getMatrix(msg = "Ingrese su matriz") -> list[list]:#Verifica que lo ingresado sea una matriz
    isDone = False
    matrix = None
    while(not isDone):
        matrix = leer_arreglo(msg)
        if(isinstance(matrix, list)): isDone = True
        else: print("Inténtelo de nuevo")
    return matrix

def leer_arreglo(msg = "Ingrese matriz"):#Pide al usuario la matriz/vector y la ingresa
    entrada = input(msg+" como 'filas,elementos...': ").strip()
    partes = entrada.split(',')
    if len(partes) < 2:
        print("Error: Formato incorrecto. Ejemplo: '2,1,2,3,4'")
        return

    filas = int(partes[0])
    elementos = [float(x) for x in partes[1:]]
    if len(elementos) % filas != 0:
        print("Error: La cantidad de elementos no es divisible por el número de filas.")
        return

    columnas = len(elementos) // filas
    array = []
    for i in range(filas):
        array.append([])
        for j in range(columnas):
            array[i].append(elementos[i * columnas + j])
    return array


#OPT 1:Suma de arreglos - Lee una matriz desde la entrada del usuario
def suma_arreglo(matriz_a, matriz_b):
    res = []
    for i in range(0, len(matriz_a)):
        res.append([])
        for j in range(0, len(matriz_a[0])):
            res[i].append(matriz_a[i][j] + matriz_b[i][j])
    return res

#OPT 2:Cambiar de forma a una matriz - Cambia la forma de una matriz
def reshape(a, FilasN, ColumnasN):
    elementos = [elem for fila in a for elem in fila] #recorre cada fila y cada columana y los guarda en una nueva lista
    if len(elementos) != FilasN * ColumnasN:  #verifica si la nueva lista tiene el mismo numero de elementos
        print("Error: La nueva forma no es compatible con el número de elementos.")
        return None
    newShape = []
    for i in range(FilasN):
        newShape.append([])
        for j in range(ColumnasN):
            newShape[i].append(elementos[i * ColumnasN + j])
    return newShape

#OPT 3:Producto punto
def ProductoPunto(v1, v2):
    if len(v1) != len(v2): #verifica que la longitud de los vectores sea igual
        print("Error: Los vectores deben tener el mismo tamaño.")
        return None
    resultado = 0
    for i in range(len(v1)):
        resultado += v1[i] * v2[i]  # Multiplicación elemento a elemento y suma acumulada
    return resultado

#Recibe un vector o matriz y lo convierte a una matriz (list[list]
def toMatrix(vectorOrMatrix: list):
    if(isinstance(vectorOrMatrix[0], list)): return vectorOrMatrix
    else: return [vectorOrMatrix]

#Recibe un vector en representación matriz (list[list]) y lo convierte a un vector (list). Ejemplo: [[1],[2],[3]] -> [1,2,3]
def toVector(vectorAsMatrix: list[list]):
    parsedVector: list = []
    if(len(vectorAsMatrix[0]) == 1): #Vertical vector
        for i in range(0, len(vectorAsMatrix)):
            parsedVector.append(vectorAsMatrix[i][0])
        return parsedVector
    elif(len(vectorAsMatrix) == 1): #Horizontal vector
        for i in range(0, len(vectorAsMatrix[0])):
            parsedVector.append(vectorAsMatrix[0][i])
        return parsedVector
    else:
        return None

#Wrapper para ProductoPunto que verifica si los argumentos son vectores válidos
def DotProductWrapper(v1: list, v2: list):
    parsedV1: list = []
    parsedV2: list = []
    if(isinstance(v1[0], list)):
        parsedV1 = toVector(v1)
    else: parsedV1 = v1
    if(isinstance(v2[0], list)):
        parsedV2 = toVector(v2)
    else: parsedV2 = v2
    if(isinstance(parsedV1, list) and isinstance(parsedV2, list)): return ProductoPunto(parsedV1, parsedV2)
    else:
        print("El producto punto solo se puede aplicar en vectores")
        return None

#OPT 4: Selecciona una columna específica de una matriz
def seleccionar_columna(matriz, columna): #matriz, Columna (indice que se quiere extraer)
    columna_resultado = []
    for fila in matriz: #recorre cada fila
        columna_resultado.append(fila[columna-1])#extrae el valor correspondiente a la columa y lo agrega a la lista
    return columna_resultado

#OPT 5: Media de una matriz - Calcula la media de todos los elementos de una matriz
def media_matriz(matriz):
    total = 0
    for fila in matriz: #recoore cada fila
        for valor in fila: #recorre cada numero de la fila
            total += valor #suma cada numero al total

    elementos = len(matriz)* len(matriz[0])

    if elementos == 0: #verifica si la matriz esta vacia. Técnicamente esto debería ser imposible pero es bueno verificar
        print("Error: La matriz está vacía.")
    return total / elementos #calcula el promedio

#OPT 7: Producto por matriz - Multiplica dos matrices
def producto_matrices(matriz_a, matriz_b):
    resultado = []
    for i in range(len(matriz_a)):  # filas de A
        fila_resultado = []
        for j in range(len(matriz_b[0])):  # columnas de B
            suma = 0
            for k in range(len(matriz_a[0])):  # columnas de A == filas de B
                suma += matriz_a[i][k] * matriz_b[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

#OPT 8: Suma de matrices - suma dos matrices elemento por elemento
def suma_matrices(matriz_a, matriz_b):
    res = [[0]*len(matriz_a[0]) for _ in range(len(matriz_a))]
    for i in range(len(matriz_a)):
        for j in range(len(matriz_a[0])):
            res[i][j] = matriz_a[i][j] + matriz_b[i][j]
    return res

# OPT 10: Inversa de una matriz - Calcula la inversa de una matriz cuadrada
def getInverse(matrix: list[list]):
    if(len(matrix) == len(matrix[0])):
        determinant = getDeterminant(matrix)
        if(determinant != 0):
            if(len(matrix) > 1 and len(matrix[0]) > 1):
                adjugate = transpose(getCofactors(matrix))
                return multiplyMatrixByNumber((1/determinant), adjugate)
            else: return [[1/matrix[0][0]]] #the inverse of a single element matrix is 1/itself
        else: return "La matriz es singular."
    else: return "La matriz no es cuadrada"

# OPT 11: Transpuesta de una matriz - Calcula la transpuesta de una matriz
def transpose(matrix: list[list]):
    transposed: list[list] = []
    for i in range(0, len(matrix[0])):
        transposed.append([])
        for j in range(0, len(matrix)):
            transposed[i].append(matrix[j][i])
    return transposed

#Escribir una matriz o vector como string
def matrixToString(matrix: list):
    matrixStr = ""
    if(isinstance(matrix[0], list)):
        for i in range(0, len(matrix)):
            matrixStr += "|\t"
            for j in range(0, len(matrix[0])):
                matrixStr += str(matrix[i][j]) + "\t"
            matrixStr += "|\n"
    elif(isinstance(matrix, list)):
        for i in range(0, len(matrix)):
            matrixStr += "|\t"+str(matrix[i])+"\t|"
            matrixStr += "\n"
    return matrixStr

# Funcion encargada de evaluar si el # de columnas de la matriz a es igual al # de filas de la matriz b
def evaluar_producto(matriz_a, matriz_b):
    if len(matriz_a[0]) == len(matriz_b):
        return True
    else:
        print("Error de dimensión")
        return False

# Funcion encargada de evaluar si la matriz a tiene el mismo tamaño que la matriz b
def evaluar_suma(matriz_a, matriz_b):
    if len(matriz_a) == len(matriz_b):
        if len(matriz_a[0]) == len(matriz_b[0]):
            return True
    else:
        print("Error de dimensión")
        return False

#OPT 6: Multiplica todos los elementos de una matriz por un escalar.
def multiplyMatrixByNumber(number, matrix: list[list]):
    result: list[list] = []
    for i in range(0, len(matrix)):
        result.append([])
        for j in range(0, len(matrix[0])):
            result[i].append(number * matrix[i][j])
    return result

# Calcula la matriz de cofactores.
def getCofactors(matrix: list[list]):
    cofactors: list[list] = []
    if (len(matrix) == len(matrix[0])):
        length = len(matrix)
        for i in range(0, length): #rows
            cofactors.append([])
            for j in range(0, length): #cols
                newMatrix = removeRowColAt(matrix ,i, j) #"Tachar" columna y fila
                currentCof = getDeterminant(newMatrix)
                if ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)): #Compensa por la matriz de signos
                    cofactors[i].append(currentCof)
                else:
                    cofactors[i].append(-currentCof)
    else:
        print("La matriz no es cuadrada!")
    return cofactors

# Elimina una fila y una columna específica de una matriz.
def removeRowColAt(matrix: list[list], row, col): #ARGS: Matriz original, fila a eliminar, columna a eliminar
    newMatrix: list[list] = []
    for i in range(0, len(matrix)-1): #Es importante que el rango sea len(matrix)-1 ya que se eliminará una fila
        if(i < row): currentRow = i #Si la fila es menor a la fila que se quiere eliminar, no se hace nada
        else: currentRow = i+1 #Si no, se suma 1 para eliminar la fila
        newMatrix.append([])
        for j in range(0, len(matrix[0])-1): #Es importante que el rango sea len(matrix[0])-1 ya que se eliminará una columna
            if(j < col): currentCol = j #Si la columna es menor a la columna que se quiere eliminar, no se hace nada
            else: currentCol = j+1 #Si no, se suma 1 para eliminar la columna
            newMatrix[i].append(matrix[currentRow][currentCol])
    return newMatrix

# Calcula el determinante de una matriz cuadrada.
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

def mainUI():
    option = -1
    while option != 0:
        option = -1 #El valor de option tiene que ser cambiado para evitar problemas al limpiar pantalla. NO ELIMINAR.
        a = getMatrix("Ingrese su primera matriz o vector")
        print(matrixToString(a))
        while option != 13 and option != 0:
            print(
                "Seleccione una opción:",
                "1: Suma de arreglos",
                "2: Cambio de forma",
                "3: Producto punto de dos vectores",
                "4: Seleccionar una columna",
                "5: Media de una Matriz",
                "6: Producto por escalar",
                "7: Multiplicacion de matrices",
                "8: Suma de matrices",
                "9: Calculo de determinante",
                "10: Inversa de una matriz",
                "11: Transpuesta de una matriz",
                "12: Resolver como sistema de ecuaciones",
                "13: Limpiar pantalla",
                "0: Salir",
                sep='\n'
            )
            option = int(input("Seleccione una opción:"))
            result = None
            match option:
                case 1:
                    b = getMatrix("Ingrese su segunda matriz")
                    result = suma_arreglo(a, b)
                case 2:
                    rows = int(input("Ingrese el número de filas: "))
                    cols = int(input("Ingrese el número de columnas: "))
                    result = reshape(a, rows, cols)
                case 3:
                    b = getMatrix("Ingrese su segundo vector")
                    result = DotProductWrapper(a, b)
                case 4:
                    col = int(input("Escoja la columna: "))
                    result = seleccionar_columna(a, col)
                case 5:
                    result = media_matriz(a)
                case 6:
                    scalar = float(input("Ingrese el escalar: "))
                    result = multiplyMatrixByNumber(scalar, a)
                case 7:
                    b = getMatrix("Ingrese su segunda matriz")
                    if evaluar_producto(a, b):
                        result = producto_matrices(a, b)
                    else :
                        print("Error: Las matrices no son compatibles para la multiplicación.")
                case 8:
                    b = getMatrix("Ingrese su segunda matriz")
                    if evaluar_suma(a, b):
                        result = suma_matrices(a,b)
                    else:
                        print("Error: La matriz no es cuadrada.")
                case 9:
                    getDeterminant(a)
                case 10:
                    result = getInverse(a)
                case 11:
                    result = transpose(a)
                case 12:
                    result = equationSystemSolver(a)
                case 13:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #"Limpia" la pantalla poniendo 3 millones de newlines

                    print("Pantalla limpiada y memoria reiniciada.") #Ref: https://www.geeksforgeeks.org/clear-screen-python/
                case 0:
                    print("Saliendo del programa...")
                case _:
                    print("Operación inválida. Intente de nuevo.")
            if(option !=13 and option != 0):
                if (isinstance(result, float) or isinstance(result, int)):
                    print('\033[92m El resultado de la operación es: \033[0m')
                    print(f'\033[92m {result} \033[0m')
                elif isinstance(result, list):
                    a = toMatrix(result)
                    print('\033[92m El resultado de la operación es: \033[0m')
                    print(f'\033[92m{matrixToString(result)} \033[0m')
                elif isinstance(result, str):
                    print('\033[92m El resultado de la operación es: \033[0m')
                    print(f'\033[92m {result} \033[0m')

#main
mainUI()