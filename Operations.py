#Parte Laura

"""Suma dos matrices elemento por elemento"""
def suma(a, b):  #Recibe dos matrices a,b
    if len(a) != len(b): #comprueba si a y b tienen la misma longitud
        print("Error: Los arreglos deben tener el mismo tamaño.")
        return
    return [a[i] + b[i] for i in range(len(a))]  #genera indices de 0 hasta la misma pposicion y lo suma


"""Cambia la forma de una matriz"""
def reshape(a, FilasN, ColumnasN):
    elementos = [elem for fila in a for elem in fila] #recorre cada gila y cala columana y los guarda en un anueva lista
    if len(elementos) != FilasN * ColumnasN:  #verifica si la nueva lista tiene el mismo numeri de elementos
        print("Error: La nueva forma no es compatible con el número de elementos.")
    return [elementos[i*ColumnasN:(i+1)*ColumnasN] for i in range(FilasN)]  #divide la lista de elemntos en sublistas de longitud ColumnasN y se crean las FilasN


"""Producto punto"""
def ProductoPunto(v1, v2):
    if len(v1) != len(v2): #verifica que la longitud de los vectores sea igual
        print("Error: Los vectores deben tener el mismo tamaño.")
        return sum(v1[i] * v2[i] for i in range(len(v1))) #Multiplica los vectores en la misma posicion y dsp los suma

from laura import *

#Parte Ricardo

"""Selecciona una columna específica de una matriz"""
def seleccionar_columna(matriz, columna): #matriz, Columna (indice que se quiere extraer)
    columna_resultado = []
    for fila in matriz: #recorre cada fila
        columna_resultado.append(fila[columna])#extrae el valor correspondiente a la columa y lo agrega a la lista
    return columna_resultado


"""Calcula la media de todos los elementos de una matriz"""
def media_matriz(matriz):
    total = 0
    for fila in matriz: #recoore cada fila
        for valor in fila: #recorre cada numero de la fila
            total += valor #suma cada numero al total

    elementos = 0
    for fila in matriz:
        elementos += len(fila)#suma la cantidad de elemntos al contador

    if elementos == 0: #verifica si la matriz esta vacia
        print("Error: La matriz está vacía.")
    return total / elementos #calcula el promedio


"""Multiplica una matriz por un escalar"""
def multiplicar_escalar(matriz, escalar):
    resultado = []
    for fila in matriz: #recorre cada fila
        nueva_fila = []
        for elemento in fila:
            nueva_fila.append(elemento * escalar)
        resultado.append(nueva_fila)
    return resultado

#Partte de Natalia



#Parte Juan Felipe (en los archivos respectivos, se importa al main para usar las funciones)
from InverseMatrix import *
from GaussJordan import *

"""Lee una matriz desde la entrada del usuario"""
def leer_arreglo(msg = "Ingrese matriz"):
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
    return [elementos[i*columnas:(i+1)*columnas] for i in range(filas)]




def mostrar_menu():
    """Muestra el menú principal"""
    print("\nMENÚ PRINCIPAL:")
    print("1. Suma de matrices")
    print("2. Cambiar forma de matriz")
    print("3. Producto punto de vectores")
    print("4. Extraer columna")
    print("5. Media de matriz")
    print("6. Multiplicar por escalar")
    print("7. Multiplicación de matrices")
    print("8. Suma de matrices (alterna)")
    print("9. Calcular determinante")
    print("10. Calcular matriz inversa")
    print("11. Transpuesta de matriz")
    print("12. Resolver sistema 2x2")
    print("13. Ingresar nueva matriz")
    print("0. Salir")

def main():
    """Función principal del programa"""
    print("=== CALCULADORA DE ARREGLOS ===")
    memoria = leer_arreglo()
