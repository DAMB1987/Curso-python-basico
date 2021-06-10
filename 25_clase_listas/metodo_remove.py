#información tomada de https://www.programiz.com/python-programming/methods/list/remove

"""
El método remove () elimina el primer elemento coincidente (que se pasa como argumento) de la lista.


La sintaxis del remove()método es:

list.remove (elemento)
remove () Parámetros
El remove()método toma un solo elemento como argumento y lo elimina de la lista.
Si elementno existe, arroja ValueError: list.remove (x): x no en la excepción de lista .
Valor devuelto de remove ()
El remove()no devuelve ningún valor (retornos None).
"""

# Ejemplo 1: eliminar elemento de la lista
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

# Updated animals List
print('Updated animals list: ', animals)
# Producción

# Lista de animales actualizada: ['gato', 'perro', 'conejillo de indias']

# Ejemplo 2: método remove () en una lista que tiene elementos duplicados
# Si una lista contiene elementos duplicados, el remove()método solo elimina el primer elemento coincidente.

# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' is removed
animals.remove('dog')

# Updated animals list
print('Updated animals list: ', animals)

# Producción

# Lista de animales actualizada: ['gato', 'perro', 'conejillo de indias', 'perro']
# Aquí, solo la primera aparición del elemento 'perro' se elimina de la lista.

# Ejemplo 3: eliminar elemento que no existe
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# Deleting 'fish' element
animals.remove('fish')

# Updated animals List
print('Updated animals list: ', animals)

# Producción

# Rastreo (llamadas recientes más última):
#   Archivo ".. .. ..", línea 5, en <módulo>
#     animal.remove ('pez')
# ValueError: list.remove (x): x no está en la lista
# Aquí, recibimos un error porque la animalslista no contiene 'fish'.

# Si necesita eliminar elementos basados ​​en el índice (como el cuarto elemento), puede usar el método pop () .
# Además, puede usar la instrucción del de Python para eliminar elementos de la lista.