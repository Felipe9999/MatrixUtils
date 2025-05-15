def producto_matrices(matriz_a, matriz_b):
    resultado = []
    for i in range(len(matriz_a)): #filas
        fila_resultado = []
        for j in range(len(matriz_b)): #columnas
            suma = 0
            for k in range(len(matriz_a)): #columnas
                suma += matriz_a[i][k] * matriz_b[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

def suma_matrices(matriz_a, matriz_b):
    #res = [[0]*len(matriz_a) for _ in range(len(matriz_a[0]))]
    res = []
    for i in range(0, len(matriz_a)):
        res.append([])
        for j in range(0, len(matriz_a[0])):
            #res[i][j] = matriz_a[i][j] + matriz_b[i][j]
            res[i].append(matriz_a[i][j] + matriz_b[i][j])
    return res
