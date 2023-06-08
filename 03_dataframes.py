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
df7 = pd.DataFrame.from_dict(data=data4)
print(df7)
df7 = pd.DataFrame.from_dict(data=data4, orient="index", columns=["A","B","C"])
print(df7)

print(df1)
print(df1.shape) # Número de filas y columnas que tiene el dataframe
print(df1.shape[0]) # Número de filas que tiene el dataframe
print(df1.shape[1]) # Número de columnas que tiene el dataframe
print(df1.size) # Número de elemetnos guardados en el dataframe
print(df1.ndim) # Número de dimensiones en el dataframe

# Seleccionando columnas
fdata = {"Name":["Alicia", "Bill", "Carlos", "Diana"],
         "Age": [22, 28, 19, 34],
         "Pet": [True, False, False, True],
         "height": [157, 190, 175, 164],
         "Birthday": ["Mayo", "Junio", "Agosto", "Diciembre"]}
df = pd.DataFrame(data=fdata, index=["obs1", "obs2", "obs3", "obs4"])
print(df)

# Seleccionamos la columna Birthday por nombre
print(df["Birthday"])

# Seleccionamos la columna Birthday con el método .columns[] indicando el indice
print(df.columns[4])

# Seleccionamos la columna Birthday con el método .loc[] por nombre
print(df.loc[:, "Birthday"])

# Seleccionamos la columna Birthday con el método .iloc[] por indice
print(df.iloc[:, 4])

# Seleccionamos mas de una columna
print(df[["Name", "Age"]])
print(df[df.columns[[0, 1]]])
print(df.loc[:, ["Name", "Age"]])
print(df.iloc[:, [0, 1]])

# Seleccionando filas
print(df.loc["obs3"])
print(df.iloc[-1])
print(df.loc[["obs1","obs2"]])
print(df.iloc[[1,-4]])

# Seleccionando elementos
print(df.loc["obs3","Birthday"])
print(df.iloc[-2, 0])

# Métodos
d = {"fruit": ["sandia", "melón", "manzana", "cerezas", "plátano", "pera", "melocotón", "fresas"],
     "count": [1, 1, 6, 10, 3, 6, 4, 10]}
df = pd.DataFrame(data=d)
print(df.head()) # Para que se muestre un numero determinado de filas empezando desde el principio, si lo dejamos vacio se muestra 5 primeras filas
print(df.tail()) # Para que se muestre un numeor determinado de filas empezando desde el final, si lo dejamos vacio se muestran los 5 ultimas filas
# Para copiar un dataframe existente a otra valirable independiente (si no se usa el metedo y solo se iguala data2 = data1, todos los cambios que hagamos en el data2 tendra reflejo en el data1)
dfnew = df.copy()
dfnew.iloc[6, 0] = "mandarina"
print(df)
print(dfnew) 

# Método .rename() se puede utilizar par cambiar el nombre de las etiquetas de las filas y como de las columnas. 
# Pero si queremos que el cambio se guarde y no que se cree una copia del mismo temporalmente, hay que poner el parametro inplace = True
df.rename(columns={"fruit":"fruta",
                   "count":"cantidad"}, inplace=True)
print(df)
df.rename(index={0:"obs1",
                 1:"obs2"}, inplace=True)
print(df)

# Método .insert() se utiliza para insertar una nueva columna en un dataframe
df.insert(loc=1, column="precio", value=[2.50, 2.00, 0.35, 0.10, 0.35, 0.20, 0.15, 0.05])
print(df)
df.insert(loc=2, column="color", value="rojo")
print(df)

# Método .drop() se usa para eliminar filas o columnas que indiquemos.
# Pero si queremos que el cambio se guarde y no que se cree una copia del mismo temporalmente, hay que poner el parametro inplace = True
# Con el parametro axis indicamos si queremos borrar filas o columnas 0 = filas, 1 = columnas
df.drop(labels="color", axis=1, inplace=True)
print(df)
df.drop(labels=4, axis=0, inplace=True)
print(df)

# Método .pop() se usa para eliminar un acolumna que se le pase por paramtero, pero si guardas el resultado en una variable, esta variable tendra el contenido de esa columna borrada.
column_popped = df.pop("precio")
print(df)
print(column_popped)

# Para añadir de forma rápida una columna al final de un dataframe
df["precio"] = column_popped
print(df)

# Método .rank() devuelve un ranking
df["Ranking_Fruta"] = df["fruta"].rank(ascending=False)
print(df)

# Método .nunique() devuelve el conteo de cuántos valores únicos hay en cada columna.
print(df.nunique())

# Método .unique() devuelve el conteo de cuántos valores únicos hay en una columna.
print(df["precio"].unique())

# Método .duplicated() analiza los valores duplicados. 
# Parametro 
# keep = first (considera la primera aparición del valor repetido como único y el resto cmo duplicados)
# keep = last (considera la última aparición del valor repetido como único y el resto como duplicados)
# keep = False (considera todos los repetidos iguales com duplicados)
bool_duplicated = df["cantidad"].duplicated(keep=False)
print(df[bool_duplicated])

# Método .nsmallest() nos devuelve las n filas con le valor mas pequeño.
print(df.nsmallest(3,"precio")) 

# Método .nlargest() nos devuelve las n filas con le valor mas grande.
print(df.nlargest(3,"cantidad")) 

# Método .dtypes nos devuelve el tipo de datos de cada columna
print(df.dtypes)


# Ejercicio1
def is_palindrome(word):
    """
    Devuelve si la palabra word es palíndroma.
    Args:
     word: Palabra en formato string
    Returns:
     isPalindrome: Booleano 
    """
    word = word.lower()
    l = []
    isPalindrome = True
    for c in word:
        l.append(c)
    n = len(l) 
    for i in range(int(n / 2)):
        if l[i] != l[n - (i + 1)]:
            isPalindrome = False
    return isPalindrome        

words = ["sol", "ala", "cama", "duro", "bueno", "kayak", "marea", "rotor", "misterio", "acurruca"]
data = {"word": words,
        "length": map(len, words),
        "start": map(lambda w: w[0], words),
        "end": map(lambda w: w[-1], words),
        "isPalindrome": map(is_palindrome, words)}
words = pd.DataFrame(data=data)
words = words.set_index("word")
words.index.names = [None]
print(words)

# Ejercicio2
print(words.head(5))
print(words.tail(5))
words_copy = words.copy()
words_copy.rename(columns={"length":"Longitud",
                           "start":"Inicio",
                           "end":"Fin",
                           "isPalindrome":"Palindromo"},inplace=True)
print(words_copy)

# Bucles y dataframes
# Métodos .iterrows() y .itertuples()
d = {"name": ["Juan Gabriel", "María", "Ricardo"],
     "surname": ["Gomila", "Santos", "Alberich"],
     "gender": ["m", "f", "m"]}
df = pd.DataFrame(d)
print(df)

# .iterrows() Iterando sobre las filas de un dataframe. Nos devuelve el indice de cada fila
for i, j in df.iterrows():
    print(f"Indice de la fíla: {i}, \n\nContenido de la fila:\n{j}\n\n\n")

# .itertuples() Iterando sobre las filas de un dataframe. Nos devuelve en formato tupla el indice de cada fila
for i in df.itertuples():
    print(f"Contenido de la fila:\n{i}\n\n")

# Iterando sobre las columnas de un dataframe.
columns = list(df)
for c in columns:
    print(f"Columna: {c}:\n{df[c]}\n\n")

# Cargando en un DataFrame CON un CSV
# Desde una url
letters_freq_df = pd.read_csv("https://raw.githubusercontent.com/witwall/gdocjdbc/master/doc/Simpsons%20Characters.csv")
print(letters_freq_df)

letters_freq_df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/letter_frequency.csv")
letters_freq_df.columns = ["Letra", "Frecuencia", "Porcentaje"]
print(letters_freq_df)

# Cargando un DataFrame con un JSON
fichero_json = pd.read_json("https://api.exchangerate-api.com/v4/latest/EUR")
print(fichero_json.head())