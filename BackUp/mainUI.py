from Operations import *

def getMatrix(msg = "Ingrese su matriz") -> list[list]:
    isDone = False
    matrix = None
    while(not isDone):
        matrix = leer_arreglo(msg)
        if(isinstance(matrix, list)): isDone = True
        else: print("Inténtelo de nuevo")
    return matrix

def matrixToString(matrix: list):
    matrixStr = ""
    if(isinstance(matrix[0], list)):
        for i in range(0, len(matrix)):
            matrixStr += "|\t"
            for j in range(0, len(matrix[0])):
                matrixStr += str(matrix[i][j]) + "\t"
            matrixStr += "|"
            if(i != len(matrixStr)-1): matrixStr += "\n"
    elif(isinstance(matrix, list)):
        for i in range(0, len(matrix)):
            matrixStr += "|\t"+str(matrix[i])+"\t|"
            if(i != len(matrixStr)-1): matrixStr += "\n"
    return matrixStr

def mainUI():
    option = -1
    while(option != 0):
        option = -1
        a = getMatrix("Ingrese su primera matriz o vector")
        print(matrixToString(a))
        while(option != 13 and option != 0):
            print(
                "Seleccione una opción:",
                "1: Suma de matrices",
                "2: Cambio de forma",
                "3: Producto punto de vectores",
                "4: Seleccionar una columna",
                "5: Media de una Matriz",
                "6: Producto por escalar",
                "7: Producto por matriz",
                "8: Calcular determinante",
                "9: Calcular inversa",
                "10: Transponer",
                "11: Reducción Gauss Jordan",
                "12: Resolver como sistema de ecuaciones",
                "13: Limpiar pantalla",
                "0: Salir",
                sep='\n'
            )
            option = int(input())
            result = None
            match option:
                case 1:
                    b = getMatrix("Ingrese su segunda matriz")
                    result = suma_matrices(a, b)
                case 2:
                    rows = int(input("Ingrese el número de filas"))
                    cols = int(input("Ingrese el número de columnas"))
                    result = reshape(a, rows, cols)
                case 3:
                    b = getMatrix("Ingrese su segunda matriz")
                    result = ProductoPunto(a, b)
                case 4:
                    col = int(input("Escoja la columna"))
                    result = seleccionar_columna(a, col)
                case 5:
                    result = media_matriz(a)
                case 6:
                    scalar = float(input("Ingrese el escalar"))
                    result = multiplicar_escalar(a, scalar)
                case 7:
                    b = getMatrix("Ingrese su segunda matriz ")
                    result = producto_matrices(a, b)
                case 8:
                    result = getDeterminant(a)
                case 9:
                    result = getInverse(a)
                case 10:
                    result = transpose(a)
                case 11:
                    result = GaussJordan(a)
                case 12:
                    result = equationSystemSolver(a)
                case 13:
                    result = None
                    #do nothing
                case 0:
                    result = None
                    #do nothing
                case _:
                    print("Operación inválida")
            if(isinstance(result, list)):
                a = result
                print(matrixToString(a))
            elif(isinstance(result, str)):
                print(result)

mainUI()