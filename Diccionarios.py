# EN ESTE SCRIPT VEREMOS COMO TRABAJAR CON LOS DICCIONARIOS
# NECESITAMOS SABER QUE LAS LISTAS SE DEFINEN CON [] Y QUE VA DE [0,N-1]
# NECESITAMOS SABER QUE TIENEN DOS VALORES --> LA CLAVE Y EL VALOR
# NECESITAMOS SABER QUE NO PUEDE HABER CLAVES DUPLICADAS


# Para definir un diccionario
diccionario={"azul":"blue", "rojo":"red", "verde":"green"}
print(diccionario)


# Imprimir el valor deuna clave
print(diccionario["rojo"])


# Añadir elementos
diccionario["amarillo"] = "yellow"
print(diccionario)


# Editar elementos
diccionario["azul"] = "Blue"
print(diccionario)


# Borrar elementos
del(diccionario["amarillo"])
print(diccionario)

# Diccionario con colecciones dentro
dic = {"Iker":[22,1.85],"Ander":[21,1.73],"Juan":[19,1.90]}
dic2 = {"Iker":{"edad":22,"estatura":1.85},"Ander":{"edad":21,"estatura":1.73},"Juan":{"edad":19,"estatura":1.90}}
print(dic2)
print(dic2["Iker"])