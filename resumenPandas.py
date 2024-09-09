import pandas as  pd
import numpy as np
#PANDAS!!!

#BUSQUEDA POR ETIQUETA (INDICE EXPLICITO) LOC
s = pd.Series([10, 20, 30, 40], index = ["b", "c","a", "d"])
print(s.loc["b"])

#ORDENAR UNA SERIE por indiceeeeeeeeeeeee!
data_sorted = s.sort_index()
print(data_sorted)

#SELECCIONANDO MÁS DE UNA ETIQUETA
s.loc[["d", "a"]]

#SELECIONANDO UN RANGO
s["b":"d"]

#BUSQUEDA POR INDICE IMPLICITO (ILOC)
i = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])
print(i.iloc[2]) #acá devuelve el valor que existe en ese indice implicito

#tambien puede acceder al incice del ultimo valor o indices negativos
s.iloc[-1]

# En este caso devuelve una lista con los valores presentes en esos indices y en el orden indicado
# Fijense el doble corchete. El par interior corresponde a una lista
s.iloc[[2, 0]]

#devuelve los  valores en ese rango (desde el primero incluido al segundo sin incluir)
s.iloc[1:3]

#si no se especifica segundo valor   llega hasta  el final
print(i.iloc[2:])

#SELECCION CON LISTA DE BOOLEANOS
b = pd.Series([5, 2, -3, 7, 8, 4])
b[[True, False, False, True, True, False]]
# 5, 7, 8

#esta lista puede ser el resultado de una expresion
print(b > 2)

print(b[b>2])

b.loc[b>2]

#si b fuera un array de numpy 
b.iloc[(b>2).values]

#pandas recomienda usar el método loc cuando trabajemos con selección basada en booleanos
s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])

#literal un sample de 3 datos
s.sample(3, random_state = 18)

#literal el 0.6 de la lista y random
s.sample(frac = 0.6, random_state = 18)

#sample pero va devolviendo el numero que sacó
s.sample(10, random_state = 18, replace = True)

# pandas.Series.pop
s.pop(1)  #elimina posicion 1

#manejo de error si es que el valor no existe
s = pd.Series([1, 2, 3, 4])
try:
    s.pop(18)
except Exception as e:
    print(e.__doc__)
    print(type(e).__name__)

#si es que la serie tiene indice  explicito, el argumento pop hace referencia a ese indice
s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])
s.pop("a")

#ACTIVIDAD 1!!
def filtrar_alturas(diccionario_alturas):
    # Convertir el diccionario en una Serie de Pandas
    serie_alturas = pd.Series(diccionario_alturas)
    
    # Filtrar alturas mayores a 1.75 metros
    alturas_filtradas = serie_alturas[serie_alturas > 1.75]

    # Ordenar las alturas de mayor a menor
    alturas_ordenadas = alturas_filtradas.sort_values(ascending=False)
    
    return alturas_ordenadas

alturas = {
    "Juan": 1.80,
    "Ana": 1.70,
    "Pedro": 1.90,
    "Lucía": 1.85,
    "Carlos": 1.60
}

resultado = filtrar_alturas(alturas)
print(resultado)

#ACTIVIDAD 2
#SELECCIONA LOS INDICES 5 Y 9
s1= pd.Series([10, 15, 20, 25, 30], index=[2, 5, 8, 9, 12])
print(s1.loc[5])
print(s1.loc[9])

#ACTIVIDAD 3
s2 = pd.Series([1, 2, 3, 4, 5], index=['a-1', 'b-2', 'c-3', 'a-4', 'b-5'])

# Filtrar los valores cuyos índices comienzan con 'a-'
resultado = s2[s2.index.str.startswith('a-')]

print(resultado)

#ACTIVIDAD 4
s3 = pd.Series(list(range(20)), index = list(range(20, 0, -1)))
# Filtrar valores cuyos índices sean impares
resultado = s3[(s3.index % 2 != 0)]
print(resultado)

#ACTIVIDAD 5
def divisibles(s):
    divisibles  = s[s%3 ==0]
    return divisibles
s4 = pd.Series(list(range(10, 101, 10)))
print(divisibles(s4))

#ACTIVIDAD 7!!!!!! AVANZADA
import datetime
dates = [datetime.date(2023, 5, 15), datetime.date(2023, 1, 10), datetime.date(2023, 3, 23),
         datetime.date(2023, 2, 15), datetime.date(2023, 8, 30), datetime.date(2023, 4, 5)]

prices = [120.5, 115.2, 112.8, 116.5, 127.4, 119.0]

#ORDENAMOS LAS FECHAS POR INDICE
data = pd.Series(prices, index=dates)
data_sorted = data.sort_index()
print(data_sorted)
print("Segunda fecha más reciente: ",data_sorted.iloc[-2])

#fecha evento importante, MOSTRAMOS LAS FECHAS POSTERIORES A ESE EVENTO
event_date = datetime.date(2023, 2, 15)
prices_after_event = data_sorted.loc[event_date:]
print(prices_after_event)

#DATAFRAMESSSSSSSSSS!!!
ventas = pd.DataFrame({
    "Entradas": [41, 32, 56, 18],
    "Salidas": [17, 54, 6, 78],
    "Valoración": [66, 54, 49, 66],
    "Límite": ["No", "Sí", "No", "No"],
    "Cambio": [1.43, 1.16, -0.67, 0.77]
},
    index = ["Ene", "Feb", "Mar", "Abr"]
)
#valores en entradas
ventas["Entradas"]
#valor entrada en febrero
ventas["Entradas"]["Feb"]
#Usar comas para separar no funciona y por lo tanto nos entrega un error.
try:
    # La separación por comas no funciona, nos entrega un error de llave
    ventas["Entradas", "Feb"]
except Exception as e:
    print(e.__doc__)
    print(type(e).__name__)

#Si, una vez seleccionada una columna, le asignamos una lista o array (o serie) de valores de la misma longitud, 
# estamos modificando dicha columna del dataframe.
ventas["Entradas"] = [33, 25, 40, 12]

#Si asignamos un único valor escalar, este se propaga por toda la columna.
ventas["Salidas"] = 1

#AGREGANDO UNA COLUMNA
# Feb no existe en la serie, luego se completa con NaN
# Mar no existe en el DataFrame, luego se descarta
ventas["Perdidas"] = pd.Series([5, 4, 6, 8], index = ["Ene", "Mar", "Abr", "May"])

#Los valores asignados pueden proceder del propio dataframe:
ventas["Ganancias"] = (ventas["Entradas"]*2) - (ventas["Valoración"]/10)

#También podemos acceder a una columna con la llamada "notación punto".
ventas.Ganancias = 1


#el método `pandas.DataFrame.loc` permite seleccionar un conjunto de filas y columnas por etiquetas
df = pd.DataFrame(np.arange(18).reshape([6, 3]),
                  index = ["a", "b", "c", "d", "e", "f"],
                  columns = ["A", "B", "C"])
df.loc["c"]
# 6, 7, 8

df = pd.DataFrame(np.arange(12).reshape([4, 3]),
                  index = [1, 3, 0, 4],
                  columns = ["A", "B", "C"])
# No es el índice cero, es la etiqueta 0
df.loc[0]

df = pd.DataFrame(np.arange(18).reshape([6, 3]),
                  index = ["a", "b", "c", "d", "e", "f"],
                  columns = ["A", "B", "C"])

df.columns.get_loc("B")
# 1
df.columns.get_indexer(["A", "C"])
#array([0, 2])
df.index.get_loc("d")
# 3

df.iloc[df.index.get_loc("c"), 2]
# 8

#si deseásemos obtener de las filas 5 y 3 (en este orden) los valores correspondientes a las columnas $C$ y $A$ 
# (en este orden), podríamos hacerlo con la siguiente expresión:
df.iloc[[5, 3], df.columns.get_indexer(["C", "A"])]

#SELECCION DE FILAS CON UNA LISTA DE BOOLEANOS
df = pd.DataFrame(np.arange(18).reshape([6, 3]),
                  index = ["a", "b", "c", "d", "e", "f"],
                  columns = ["A", "B", "C"])
print(df)
mask = [True, False, True, False, False, True]
df[mask]

#APLICAMOS FUNCION  DIRECTA
df.loc[df.B > 6]


df = pd.DataFrame(np.arange(18).reshape([6, 3]),
                  index = ["a", "b", "c", "d", "e", "f"],
                  columns = ["A", "B", "C"])
df.sample(3, random_state = 18)

#Si especificamos como eje el valor 1, estaremos extrayendo columnas.
df.sample(2, random_state = 18, axis = 1)

#Si hacemos uso del parámetro `frac`, podemos especificar el porcentaje de elementos a extraer.
df.sample(frac = 0.6, random_state = 18)

#Otra forma de EXTRAER es el método `pandas.DataFrame.pop`, que extrae y elimina una columna de un dataframe.
df = pd.DataFrame(np.arange(15).reshape([3, 5]),
                  index = ["a", "b", "c"],
                  columns = ["A", "B", "C", "D", "E"])
columna = df.pop("B")
columna
#DEVUELVE LOS DATOS DE LA COLUMNA B


#ACTIVIDAD 3
# Crear el DataFrame
df2 = pd.DataFrame(np.random.randint(0, 100, size=(8, 4)), columns=list('WXYZ'))
print(df2)
# Seleccionar las filas de índice 2 a 5 y solo las columnas 'W' y 'Z'
selected_df = df2.loc[2:5, ['W', 'Z']]
print(selected_df)


#ACTIVIDAD 4 !!!!
data = {
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randint(1, 10, 8),
    'D': np.random.randint(1, 10, 8)
}
df3 = pd.DataFrame(data)
# Seleccionar registros donde A sea 'foo' y B no sea 'three'
filtered_df = df3[(df3['A'] == 'foo') & (df3['B'] != 'three')]

print(filtered_df)




#ACTIVIDAD 8!!!!!!!  AVANZADA

# Crear la Serie de auditorías
audit_dates = pd.Series(pd.to_datetime(['2023-01-15', '2023-03-05', '2023-06-20', '2023-08-25']))

# Crear el DataFrame de registros
dates = pd.date_range('20230101', '20230930', freq='D')
data = {
    'sales': np.random.randint(50, 200, len(dates)),
    'stock': np.random.randint(100, 500, len(dates)),
    'returns': np.random.randint(1, 50, len(dates))
}
df = pd.DataFrame(data, index=dates)

# Identificar las fechas de auditoría en el DataFrame
audit_sales_stock = df[df.index.isin(audit_dates)]
print(audit_sales_stock)

# Inicializar una lista para almacenar los resultados
windowed_data = []

# Definir la ventana
window_size = 2

# Iterar sobre las fechas de auditoría
for audit_date in audit_dates:
    start_date = audit_date - pd.Timedelta(days=window_size)
    end_date = audit_date + pd.Timedelta(days=window_size)
    windowed_data.append(df.loc[start_date:end_date])

# Concatenar todos los DataFrames en uno solo
windowed_df = pd.concat(windowed_data)
#print(windowed_df)

# Calcular el promedio de ventas y existencias en el DataFrame original
average_sales = df['sales'].mean()
average_stock = df['stock'].mean()

# Filtrar los datos en base a las condiciones
filtered_data = windowed_df[(windowed_df['sales'] < average_sales) & (windowed_df['stock'] > average_stock)]
print(filtered_data)

# Crear una columna "audit_period" inicializada en False
df['audit_period'] = False

# Marcar los registros que caen dentro de las ventanas de auditoría
for audit_date in audit_dates:
    start_date = audit_date - pd.Timedelta(days=window_size)
    end_date = audit_date + pd.Timedelta(days=window_size)
    df.loc[start_date:end_date, 'audit_period'] = True

#print(df)