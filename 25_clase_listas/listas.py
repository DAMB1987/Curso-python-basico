#listas

"""
Las listas son dinamicas, ya que se pueden borrar o agregar elementos
Las listas pertenecen a un conjunto llamado las estructurasde datos, son formas que nos brindan los lenguajes de programación, para guardar varios valores en una variable pero con diferente formato.

Las listas son las más intuitivas, que nos permiten guardar varios tipos de valoresdentro de una misma caja y dentro de una misma variable

"""

numeros[1, 3, 6, 8, 9, 45, 90]
print(numero)

#result
#   numeros[1, 3, 6, 8, 9, 45, 90]

#lista puede tener datos de un mismo tipo o de diferente tipo, string, entero, booleano

objetos = ["hola", 3, 4.5, True]  #la , sirve para separar elementos
objetos
#result
#"hola, 3 , 4 , 5, True"

"""
¿Comó acceder a los elementos de una lista?
con los indices
"""
objetos[1] # porque en programación se inicia desde el 0
#result 3

objetos[0]
#result hola

"""
Metodos son funciones especiales que están ligadas a un tipo de dato en particular
.append() = agregar un elemento, puede ser False o un número
.pop(), sirve para eliminar un elemento de la lista.
"""
objetos = ["hola", 3, 4.5, True]

#agregar un False a la lista, se hace con el metodo .append

objetos.append(False)
#result  ["hola", 3, 4.5, True, False]

#borrar elementos de la lista, se hace con el metodo .pop

objetos = ["hola", 3, 4.5, True]
objetos.pop(3)
#result ["hola", 4.5, True]

"""
Recorrer la lista con el ciclo for
"""

for elemento in objetos:
    print(elemento)
    #imprime cada elemento en un ciclo
    #result
    #hola
    #4.5
    #True
    #False
    #1

    """
    ¿Como escribir un elemento(nombre) al revés?
    [::-1]
    """

    objetos[::-1]
    #result [1, False, True, 4.5, "hola"]

"""
Usar un slice en las listas
"""

objetos[1:3]
#result [4.5 , True]

"""
sumar caracteres
"""
numeros2 = [6, 7, 8, 9]
#tenemos dos listas de numeros, numeros y numeros2

numeros
#result [1, 2, 3, 4, 5]

numeros2
#result [6, 7, 8, 9]

lista_final =numeros + numeros2
lista_final
#result [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
multiplicar una lista
"""
numeros * 5
#result [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]