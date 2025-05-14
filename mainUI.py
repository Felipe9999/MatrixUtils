from Operations import *

def getMatrix() -> list[list]:
    raise NotImplementedError("No se ha implementado la creación de matrices")#TODO: Implemtentar la creación de matrices

def mainUI():
    option = -1
    while(option != 0):
        a = getMatrix()
        while(option != 13):
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
            result = None
            match option:
                case 1:
                    b = getMatrix()
                    result = suma(a, b)
                case 2:
                    rows = int(input("Ingrese el número de filas"))
                    cols = int(input("Ingrese el número de columnas"))
                    reshape(a, rows, cols)
                #TODO: Add all the other cases
                case _:
                    print("Operación inválida")
