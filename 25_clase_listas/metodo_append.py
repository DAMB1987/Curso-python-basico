#información tomada de https://www.programiz.com/python-programming/methods/list/append

"""
La sintaxis del append()método es:

list.append (elemento)
append () Parámetros
El método toma un solo argumento

Articulo - un elemento que se agregará al final de la lista
El elemento puede ser números, cadenas, diccionarios, otra lista, etc.

Valor devuelto de append ()
El método no devuelve ningún valor (devuelve None).

"""

#Ejemplo 1: agregar un elemento a una lista
# animals list
animals = ['cat', 'dog', 'rabbit']

# 'guinea pig' is appended to the animals list
animals.append('guinea pig')

# Updated animals list
print('Updated animals list: ', animals)

# Producción

# Lista de animales actualizada: ['gato', 'perro', 'conejo', 'conejillo de indias']
# Ejemplo 2: Agregar una lista a una lista

# animals list
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox']

# appending wild_animals list to the animals list
animals.append(wild_animals)

print('Updated animals list: ', animals)

# Producción

# Lista de animales actualizada: ['gato', 'perro', 'conejo', ['tigre', 'zorro']]
# Es importante notar que, un solo elemento (animales salvajes lista) se agrega a la animales lista en el programa anterior.

# Si necesita agregar elementos de una lista a otra lista (en lugar de la lista en sí), use el método extend () .