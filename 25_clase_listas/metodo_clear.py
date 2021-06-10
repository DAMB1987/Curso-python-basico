#información tomada de https://www.programiz.com/python-programming/methods/list/clear

"""
El método clear () elimina todos los elementos de la lista.

La sintaxis del clear()método es:

list.clear ()
clear () Parámetros
El clear()método no toma ningún parámetro.

Valor de retorno de clear ()
El clear()método solo vacía la lista dada . No devuelve ningún valor.

"""

#Ejemplo 1: funcionamiento del método clear ()
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()

print('List:', list)

# Producción

# Lista: []
# Nota: Si está utilizando Python 2 o Python 3.2 y versiones anteriores, no puede utilizar el clear()método. En su lugar, puede utilizar el operador del.

# Ejemplo 2: Vaciar la lista usando del
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]

print('List:', list)

# Producción

# Lista: []
# Visite esta página para aprender cómo delfunciona el operador en Python.