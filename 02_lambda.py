### lambda ###

plus10 = lambda x: x + 10
print(plus10(5))

prod = lambda x, y: x * y
print(prod(5, 10))

discrimiante = lambda a, b, c: b ** 2 - 4 * a * c
print(discrimiante(5, 7, 9))

nums = [49, 57, 62, 147, 2101, 22]
lista = list(filter(lambda x: (x % 7 == 0), nums))
print(lista)