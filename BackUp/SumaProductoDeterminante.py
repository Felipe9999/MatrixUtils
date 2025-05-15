class calculadora_de_matrices:

    def __init__(self,matriz_a,matriz_b):
        self.matriz_a = matriz_a
        self.matriz_b = matriz_b

    def evaluar_suma(self):
        if len(self.matriz_a) == len(self.matriz_b):
            if len(self.matriz_a[0]) == len(self.matriz_b[0]):
                return True
        else:
            print("Error de dimensión")
            return False

    def evaluar_producto(self):
        if len(self.matriz_a[0]) == len(self.matriz_b):
            return True
        else:
            print("Error de dimensión")
            return False

    def evaluar_determinante(self, matriz):
        if len(matriz[0]) == len(matriz):
            return True
        else:
            print("Error de dimensión")
            return False


    def suma_matrices(self):
        res = [[0]*len(self.matriz_a) for _ in range(len(self.matriz_a[0]))]
        for i in range(len(self.matriz_a)):
            for j in range(len(self.matriz_a[0])):
                res[i][j] = self.matriz_a[i][j] + self.matriz_b[i][j]
        return res

    def producto_matrices(self):
        resultado = []
        for i in range(len(self.matriz_a)): #filas
            fila_resultado = []
            for j in range(len(self.matriz_b)): #columnas
                suma = 0
                for k in range(len(self.matriz_a)): #columnas
                    suma += self.matriz_a[i][k] * self.matriz_b[k][j]
                fila_resultado.append(suma)
            resultado.append(fila_resultado)
        print(resultado)

    def determinante_matrices(self, matriz):
        n = len(matriz)
        det = 1.0
        intercambios = 0

        for i in range(n):
            # Buscar el pivote: si el elemento en la diagonal es 0, buscar abajo
            if matriz[i][i] == 0:
                for k in range(i + 1, n):
                    if matriz[k][i] != 0:
                        matriz[i], matriz[k] = matriz[k], matriz[i]
                        intercambios += 1
                        break
                else:
                    det = 0
                    break

            # Hacer ceros debajo del pivote
            for j in range(i + 1, n):
                if matriz[j][i] == 0:
                    continue
                factor = matriz[j][i] / matriz[i][i]
                for k in range(i, n):
                    matriz[j][k] = matriz[j][k] - factor * matriz[i][k]

        # Multiplicar los elementos de la diagonal
        for i in range(n):
            det *= matriz[i][i]

        # Ajustar por intercambio de filas (cambia el signo del determinante)
        if intercambios % 2 != 0:
            det = -det

        return det

    def calculadora(self, operacion):
        if operacion == "suma":
            if self.evaluar_suma():
                matriz_final = self.suma_matrices()
                print("La matriz resultante es: ", matriz_final)
                return matriz_final

        if operacion == "producto":
            if self.evaluar_producto():
                matriz_final = self.producto_matrices()
                print("La matriz resultante es: ", matriz_final)
                return matriz_final

        if operacion == "determinante":
            eleccion = int(input("Elija una Matriz para calcular su determianante, las opciones son: (1)Matriz A o (2)Matriz B "))
            if eleccion == 1:
                if self.evaluar_determinante(matriz=self.matriz_a):
                    matriz_final = self.determinante_matrices(matriz=self.matriz_a)
                print("La matriz resultante es: ", matriz_final)
                return matriz_final
            elif eleccion == 2 :
                if self.evaluar_determinante(matriz=self.matriz_b):
                    matriz_final = self.determinante_matrices(matriz=self.matriz_b)
                print("La matriz resultante es: ", matriz_final)
                return matriz_final
            else:
                print("la opcion seleccionada no existe, intentelo nuevamente")
            return



mi_calculadora = calculadora_de_matrices(matriz_a = [[1,1,-5],[2,3,0],[7,0,-3]], matriz_b = [[1,9,7],[8,1,2],[-1,0,0]])
mi_calculadora.calculadora(operacion = "producto")

3,1,4,7,10,2,5,8,11,3,6,9,12