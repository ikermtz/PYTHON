# EN ESTE SCRIPT VEREMOS COMO TRABAJAR CON LAS TUPLAS
# NECESITAMOS SABER QUE LAS TUPLAS SE DEFINEN CON () Y QUE VA DE [0,N-1]
# NECESITAMOS SABER QUE EN LAS TUPLAS NO PODEMOS AÑADIR, ELIMINAR O MODIFICAR ELEMENTOS


# Para definir una tupla
tupla = ()
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]


# Transformar tupla a lista
lista = list(dias)


# Transformar lista a tupla
dias2 = tuple(lista)

# Imprimir por pantalla todos los elementos de la tupla
print(dias)

# Imprimir por pantalla un unico elemento de la tupla
print(dias[0])


# Imprimir por pantalla un unico elemento de la tupla empezando desde atras
# Empezando desde atras el primer elemento seria el -1, y el primero -N
print(dias[-1])


# Imprimir por pantalla un rango de elementos de la tupla
# Imprimir los tres primeros dias --> [0,1,2]
print(dias[0:3])
# Imprimir tres dias --> [1,2,3]
print(dias[1:4])


# Numero de elementos de la tupla
print(len(dias))


# Buscar si esta en la tupla
print("Lunes" in dias) # Dara true
print("Lunes" in tupla) # Dara false


# Buscar en que indice esta un elemento
print(dias.index("Viernes"))


# Buscar cuantas veces esta un elemento
print(dias.count("Viernes"))


