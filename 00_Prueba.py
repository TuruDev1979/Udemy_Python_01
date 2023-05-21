# Numeros complejos
z = complex(5, 6)
print(z.real)
print(z.imag)

# Métodos booleanos sobre string
s = "En un jugar de la Mancha, de cuyo nombre no quiero acordarme"
print(s.startswith("e")) # Analiza como empieza un string.
print(s.startswith("E"))
print(s.endswith(".")) # Analiza como termina un string.
print(s.endswith("acordarme"))
print(s.isalnum()) # analiza si el string es alfanumerico.
print(s.isalpha()) # Analiza si el string son letras del afabeto.
print(s.isdigit()) # Analiza si el string es un número.
print(s.isspace()) # Analiza si el string es espacios.
print(s.islower()) # Analiza si el string esta completamente en minuscula
print(s.isupper()) # Analiza si el string esta completamente en mayusculas
print(s.istitle()) # Analiza si cada palabra del string empieza en mayusculas y el resto está en minusculas.

# Como buscar algo dentro de una cadena de caracteres.
s = "Mi gato mola mucho"
c = "m"
if c in s:
    print(f"En mi string hay {s.count(c)} espacios en blanco")

# Operadores Ternarios  -- Hacer un IF en una sola linea <acciones si es verdadera> [condición if] <acciones si es falsa la condicion>



for i in range(1,11,3):
    print(i)

for i in range(20,0,-1):
    print(i)

for i in range(1, 21):
    print(f"Esta es la tabla de multiplicar del {i}")
    for x in range(1,11):
        print(f"{i} x {x} = {i * x}")



""" n = int(input("Introduce el tamaño de la lista: "))
l = []
for i in range(n):
    l.append(i)
print(f"La lista es: {l}") """