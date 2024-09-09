import numpy as np
import pandas as pd

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3],[4, 5, 6]])
c = np.array([[[1, 2, 3],[4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])

#crear matriz random con un random
rng = np.random.default_rng()
tablero = rng.integers(5, size=(3,3)) 
print(tablero)

#CREACION VECTOR Y MATRIZ CEROS
vector_ceros = np.zeros(5)
matriz_ceros = np.zeros((2,5))

matriz_unos = np.ones((2,5))

#Matriz Vacia
np.empty(5)

#Vector dentro  de un rango
np.arange(4)

#Vector en un rango (3, 10) con salto de 2 en 2
np.arange(3, 10, 2)

#matriz del 0 al 15, con 5 valores espaciados de forma equivalente
np.linspace(0, 15, num=5)

# dtype= np.int64 -> especifica que serán numeros  enteros
x = np.ones(5, dtype=np.int64)

#Matriz identidad
np.identity(3)

# Ejercicio 1, matriz de 3,3  llena de 3,5
m = np.full((3,3), [3.5])

#SUMA DE MATRICES
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 3, 6, 8, 1])
a + b

#Suma de los elementos de una matriz
a = np.array([1, 2, 3, 4])
a.sum()

# Suma por columnas (colapsa las filas) (b era la matriz)
#b.sum(axis=0)

# Suma por filas (colapsa las columnas)
#b.sum(axis=1)

# Multiplicacion elemento x elemento, (1*2, 1*4, 2*3, 1*4)
a = np.array( [[1,1],[2,1]] )
b = np.array( [[2,4],[3,4]] )
print(a)
print(b)
a * b

# MULTIPLICACION DE MATRICES 
a @ b
a.dot(b)

#Division elemento * elemento
a / b

# OTRAS  OPERACIONES
a = np.array([20,30,40,50])
b = np.arange(4)
# Elevar a una potencia
c = b**2
print(c)
print()
# Función seno
c = 10 * np.sin(a)
print(c)
print()
# Funciones lógicas, (TRUE, FALSE)
c = a < 35
print(c)

# Mínimo
b = a.min()
print(b)
print()
# Máximo
b = a.max()
print(b)
print()


# Máximo por columna
#b = a.max(axis=1)
print(b)
print()
# Media
b = a.mean()
print(b)
print()

# Desviación estándar
b = a.std()
print(b)
print()

#ORDENAR UN ARRAY
arr = np.array([2, 1, 5, 10, 3, 7, 4, 9, 6, 8])
np.sort(arr)
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

#AGREGAR ELEMENTOS DE OTRO ARRAY
#c = np.concatenate((a, b))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

#CONCATENA 2 ARREGLOS EN FILAS HACIA ABAJO
r =np.concatenate((x, y), axis=0)
print(r)

arr_ejemplo = np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],
                        [[0, 1, 2, 3],[4, 5, 6, 7]],
                        [[0 ,1 ,2, 3],[4, 5, 6, 7]]])
#Nro de dimensiones
arr_ejemplo.ndim
#NUMERO TOTAL DE ELEMENTOS DE UN ARREGLO
arr_ejemplo.size
#Entrega una tupla con el orden dee la matriz
arr_ejemplo.shape

# reshape() cambia la forma del arreglo sin alterar sus elementos
#b = a.reshape(3, 2)
#trasponer
arr.transpose()

#AGREGAR NUEVOS EJES(DIMENSIONES) A UN ARREGLO
#conveertimos en vector fila
a = np.array([1, 2, 3, 4, 5, 6, 7])
a2 = a[np.newaxis, :]
print(a2.shape)

#convertimos en vector columna
col_vector = a[:, np.newaxis]
print(col_vector)
col_vector.shape

#expandir un arreglo insertando un nuevo eje en una posición específica con la función `np.expand_dims()
a = np.array([1, 2, 3, 4, 5, 6])
b = np.expand_dims(a, axis=1)
print(b.shape)

#ENCONTRAR ELEMENTOS UNICOS, DEVUEELVE UNA LISTA SIN REPETICIONES
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
valores_unicos = np.unique(a)
print(valores_unicos)

#OBTENER EL EL INDICE ORIGINAL DE LOS VALORES DE LA LISTA SIN REEPETICIONES
valores_unicos, indices_list = np.unique(a, return_index=True)
print(indices_list)

#OBTENER CUANTAS VECES SE REPITE UN VALOR 
valores_unicos, contar_ocurrencia = np.unique(a, return_counts=True)
print(contar_ocurrencia)

#APLICAR UNA FUNCION SOBRE UNA DE LAS DIMENSIONES  DE UN  ARREGLO
arr = np.arange(1, 10).reshape(3,3)
print(arr)
np.apply_along_axis(sum, 0, arr)
