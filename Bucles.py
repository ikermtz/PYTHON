# EN ESTE SCRIPT VEREMOS COMO TRABAJAR CON LOS BUCLES

import math

numeros = [0,1,2,3,4,5,6,7,8,9]

# WHILE
i=0
todos = []
while i<10:
    todos.append(numeros[i])
    i=i+1

print("Usando while")
print(todos)


# FOR
todos2=[]
for i in numeros:
    todos2.append(numeros[i])

print("Usando for")
print(todos2)