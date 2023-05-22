### lambda ###

plus10 = lambda x: x + 10
print(plus10(5))

prod = lambda x, y: x * y
print(prod(5, 10))

discrimiante = lambda a, b, c: b ** 2 - 4 * a * c
print(discrimiante(5, 7, 9))

# filter: aplica un filtro sobre un campo itereble, segun la función informada.
nums = [49, 57, 62, 147, 2101, 22]
lista = list(filter(lambda x: (x % 7 == 0), nums))
print(lista)


# reduce: de un campo itereble a una solo valor, aplicando la función informada.
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
reduccion = reduce(lambda x, y: x * y, nums)
print(reduccion)

# Ejercicio con reduce: de una lista iterable de palabras devolver la palabra que mas "a" contenga.
def total_a(w):
    a = 0
    for letra in w.lower():
        if letra == "a":
            a += 1
    return a

def more_a(w1, w2):
    if total_a(w1) >= total_a(w2):
        return w1
    else:
        return w2
    
words = ["amapola","amigo","anastasia","flora","felpudo","casa"]
resultado = reduce(lambda w1, w2: more_a(w1, w2), words)
print(resultado)

# map: aplica una función a cada elemento de un objeto iterable.
words = ["zapato", "amigo", "yoyo", "barco", "xilófono", "césped"]
resultado = list(map(lambda w: len(w), words))
print(resultado)

# Ejercicio con map: transformar de un obejeto iteralbe de grados celsius a fahrenheit
def from_c_to_f(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

celsius = [0, 5, 10, 15, 20, 25, 50, 100, 200]
resultado = list(map(from_c_to_f, celsius))
print(resultado)

# sorted: ordena un objeto itereable segun una función
words = ["zapato", "amigo", "yoyo", "barco", "xilófono", "césped"]
resultado = sorted(words, key=lambda x: len(x), reverse=True)
print(resultado)




from numpy import random
print(random.randint(10))
print(random.randint(5, 12, size=20))
