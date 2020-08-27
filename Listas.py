
#CREACION DE LISTAS


#PERTENECE A ANA CECILIA PRIETO GRUPO 1
#listas
lista=[]
print(lista)

#lista semana
listadias=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print(listadias[0])

#lista semana
listadias=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print(listadias[-1])


#lista semana
listadias=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print(listadias[0,3])

#quitar los elementos repetidos de una lista
lista1=[1,2,3,4,"hola",2,2]
conjunto=set(lista1)
listaa=lista1(conjunto)
print(conjunto)

#listas palabras de 2 listas
lista1palabras=["ZARA","NIÑA","THOR","ODIN","NEGRA","DANTE"]
lista2palabras=["LORD","RONALDO","ODIN","ANGEL","CHANDITA","CANELA"]
print(lista1palabras,lista2palabras)

#listas de palabras que aparecen en la primera lista
lista1palabras=["ZARA","NIÑA","THOR","ODIN","NEGRA","DANTE"]
lista2palabras=["LORD","RONALDO","ODIN","ANGEL","CHANDITA","CANELA"]
print(lista1palabras[1,2,4,5],lista2palabras)

#listas de palabras que aparecen en la segunda lista
lista1palabras=["ZARA","NIÑA","THOR","ODIN","NEGRA","DANTE"]
lista2palabras=["LORD","RONALDO","ODIN","ANGEL","CHANDITA","CANELA"]
print(lista2palabras[0,1,4,5],lista1palabras)


#listas palabras repetidas en ambas listas
lista1palabras=["ZARA","NIÑA","THOR","ODIN","NEGRA","DANTE"]
lista2palabras=["LORD","RONALDO","ODIN","ANGEL","CHANDITA","CANELA"]
print(lista1palabras,lista2palabras[0,3])
