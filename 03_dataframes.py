### dataframes ###

import pandas as pd

# DataFrame desde un diccionario
data1 = {"x":[1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]}
df1 = pd.DataFrame(data=data1)
print(df1)

# DataFrame desde una lista
data2 = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]]
df2 = pd.DataFrame(data=data2, columns=["x", "y"])
print(df2)

# DataFrame desde un diccionario pero moficando el nombre de las filas
df3 = pd.DataFrame(data=data1,index=["obs1","obs2","obs3","obs4","obs5"])
print(df3)

# DataFrame usando la funcion Zip de dos listas separadas
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
data = list(zip(x, y))
print(data)
df5 = pd.DataFrame(data=data,columns=["x", "y"])
print(df5)

# Creando DataFrame a partir de un dicionario con el método from_dict
data3 = {"a": [1,2,3],
         "b": [4,5,6],
         "b1": [7,8,9]}
df6 = pd.DataFrame.from_dict(data3)
print(df6)

data4 = {"fila1": [1,2,3],
         "fila2": [4,5,6],
         "fila3": [7,8,9]}
df7 = pd.DataFrame.from_dict(data=data4, orient="index", columns=["A","B","C"])
print(df7)


print(df1.shape) # Número de filas y columnas que tiene el dataframe
print(df1.shape[0]) # Número de filas que tiene el dataframe
print(df1.shape[1]) # Número de columnas que tiene el dataframe
print(df1.size) # Número de elemetnos guardados en el dataframe
print(df1.ndim) # Número de dimensiones en el dataframe
