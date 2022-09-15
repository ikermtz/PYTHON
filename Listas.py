# EN ESTE SCRIPT VEREMOS COMO TRABAJAR CON LAS LISTAS
# NECESITAMOS SABER QUE LAS LISTAS SE DEFINEN CON [] Y QUE VA DE [0,N-1]


# Para definir una lista:
lista = []
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
numeros = [1,2,3,4,5]


# Imprimir por pantalla todos los elementos de la lista
print(dias)


# Imprimir por pantalla un unico elemento de la lista
print(dias[0])


# Imprimir por pantalla un unico elemento de la lista empezando desde atras
# Empezando desde atras el primer elemento seria el -1, y el primero -N
print(dias[-1])


# Imprimir por pantalla un rango de elementos de la lista
# Imprimir los tres primeros dias --> [0,1,2]
print(dias[0:3])
# Imprimir tres dias --> [1,2,3]
print(dias[1:4])


# Numero de elementos de la lista
print(len(dias))


# Añadir elementos al final de la lista
numeros.append(6)
print(numeros)


# Añadir elementos en una posicion especifica --> (posicion,elemento)
numeros.insert(4,4.5) #ponemos 4.5 entre el 4 y el 5
print(numeros)


# Añadir varios elementos al final de la lista
numeros.extend([7,8,9])
print(numeros)


# Concatenar listas
lista1 = [0,1,2]
lista2 = [3,4,5]
lista3 = lista1+lista2
print(lista3)


# Buscar un elemento en la lista
print(7 in numeros) # Dara true
print(14 in numeros) # Dara false


# Buscar el indice de un elemento
print(numeros.index(5))


# Contar apariciones de un elemento en la lista
print(numeros.count(4))


# Eliminar el ultimo elemento de la lista
numeros.pop()
print(numeros)


# Eliminar un elemento especifico de la lista
numeros.pop(8)
print(numeros)

# Eliminar un elemento especifico sin pasar el indice
numeros.remove(7)
print(numeros)


# Vaciar la lista
lista3.clear()
print(lista3)


# Dar la vuelta al orden de elementos
lista1.reverse()
print(lista1)


# Ordenar la lista
lista1.sort()
print(lista1)