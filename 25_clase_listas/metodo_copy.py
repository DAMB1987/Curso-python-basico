#información tomada de https://www.programiz.com/python-programming/methods/list/copy

"""
El método copy () devuelve una copia superficial de la lista.

Se puede copiar una lista con el =operador. Por ejemplo,

old_list = [1, 2, 3]
New_list = old_list
El problema de copiar listas de esta manera es que si modifica lista nueva, lista_antiguatambién se modifica. Es porque la nueva lista hace referencia o apunta a la mismalista_antigua objeto.
"""

old_list = [1, 2, 3]
new_list = old_list

# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)

# Producción

# Lista anterior: [1, 2, 3, 'a']
# Nueva lista: [1, 2, 3, 'a']
# Sin embargo, si necesita que la lista original no cambie cuando se modifica la nueva lista, puede usar el copy()método.

# Tutorial relacionado: Copia superficial de Python frente a copia profunda

# La sintaxis del copy()método es:

# new_list = list.copy ()
# copiar () parámetros
# El copy()método no toma ningún parámetro.

# Valor devuelto de copia ()
# El copy()método devuelve una nueva lista. No modifica la lista original.

# Ejemplo 1: copia de una lista
# mixed list
my_list = ['cat', 0, 6.7]

# copying a list
new_list = my_list.copy()

print('Copied List:', new_list)

# Producción

# Lista copiada: ['gato', 0, 6.7]
# Si modifica el lista nueva en el ejemplo anterior, mi lista no se modificará.

# Ejemplo 2: Copiar lista usando la sintaxis de corte
# shallow copy using the slicing syntax

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)

# Producción

# Lista anterior: ['gato', 0, 6.7]
# Nueva lista: ['gato', 0, 6.7, 'perro']