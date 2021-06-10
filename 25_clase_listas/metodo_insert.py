#información tomada de https://www.programiz.com/python-programming/methods/list/insert

"""
El método list insert () inserta un elemento en la lista en el índice especificado.

La sintaxis del insert()método es

list.insert (i, elem)
Aquí, elem se inserta en la lista en el i thíndice. Todos los elementos posteriores elemse desplazan hacia la derecha.

Insertar () Parámetros
El insert()método toma dos parámetros:

índice : el índice donde se debe insertar el elemento
elemento : este es el elemento que se insertará en la lista
Notas:

Si índice es 0, el elemento se inserta al principio de la lista.
Si índice es 3, el índice del elemento insertado será 3 (cuarto elemento de la lista).
Valor de retorno de insertar ()
El insert()método no devuelve nada; devuelve None. Solo actualiza la lista actual.

"""

# Ejemplo 1: Insertar un elemento en la lista

# vowel list
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')

print('Updated List:', vowel)
# Producción

# Lista actualizada: ['a', 'e', ​​'i', 'o', 'u']

# Ejemplo 2: Insertar una tupla (como elemento) en la lista
mixed_list = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list
mixed_list.insert(1, number_tuple)

print('Updated List:', mixed_list)

# Producción

# Lista actualizada: [{1, 2}, (3, 4), [5, 6, 7]]