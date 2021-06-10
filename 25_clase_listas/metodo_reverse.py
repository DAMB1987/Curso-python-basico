#información tomada de https://www.programiz.com/python-programming/methods/list/reverse

"""
El método reverse () invierte los elementos de la lista.


La sintaxis del reverse()método es:

list.reverse ()
parámetro reverse ()
El reverse()método no acepta argumentos.

Valor devuelto de reverse ()
El reverse()método no devuelve ningún valor. Actualiza la lista existente.

"""

# Ejemplo 1: invertir una lista
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# List Reverse
systems.reverse()

# updated list
print('Updated List:', systems)
# Producción

# Lista original: ['Windows', 'macOS', 'Linux']
# Lista actualizada: ['Linux', 'macOS', 'Windows']
# Hay otras formas de invertir una lista.

# Ejemplo 2: invertir una lista mediante el operador de corte
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list	
#Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]

# updated list
print('Updated List:', reversed_list)

# Producción

# Lista original: ['Windows', 'macOS', 'Linux']
# Lista actualizada: ['Linux', 'macOS', 'Windows']
# Ejemplo 3: Acceso a elementos en orden inverso
# Si necesita acceder a elementos individuales de una lista en orden inverso, es mejor usar reversed()function.

# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)
# Producción

# Linux
# Mac OS
# windows