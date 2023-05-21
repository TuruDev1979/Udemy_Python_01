### numpay ###
import numpy as np

a = np.empty((2, 3))
print(a)

b = np.empty_like(a)
print(b)

c = np.zeros((3, 5))
print(c)

d = np.zeros_like(a)
print(d)

e = np.ones((3, 5))
print(e)

f = np.ones_like(a)
print(f)

g = np.matrix([[1,0,-3],[2,-5,2],[-5,0,-3],[7,4,-5]])
print(g)

print(g.shape)

a = np.matrix([[1,0,-3],[2,-5,2],[-5,0,-3],[7,4,-5]])
b = np.matrix([[1,0,-3],[2,-5,2],[-5,0,-3],[7,4,-5]])
print(a + b)

a = np.matrix([[1,0,-3,2],[2,0,1,1],[-1,0,-1,0]])
b = np.matrix([[-1,-2,0],[-2,3,0],[0,0,-3],[1,1,-1]])
print(a.dot(b))

### ejercicio ###

f = int(input("Número de filas: "))
c = int(input("Número de columnas: "))

a = np.empty((f, c))

for i in range(f):
    for j in range(c):
        a[i, j] = float(input(f"Introduce el elemento {i},{j}"))

print("\n=== Matriz A ===")
print(a)