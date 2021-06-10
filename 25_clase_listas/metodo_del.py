#información tomada de https://www.programiz.com/python-programming/del

"""
La sintaxis de la deldeclaración es:

del obj_name
Aquí delhay una palabra clave de Python. Y,obj_name pueden ser variables, objetos definidos por el usuario, listas, elementos dentro de listas, diccionarios, etc.
"""

#Ejemplo 1: eliminar un objeto definido por el usuario

class MyClass:
    a = 10
    def func(self):
        print('Hello')

# Output: 
print(MyClass)

# deleting MyClass
del MyClass

# Error: MyClass is not defined
print(MyClass)	

# En el programa, hemos eliminado Mi clase utilizando del MyClass declaración.

# Ejemplo 2: eliminar variable, lista y diccionario

my_var = 5
my_tuple = ('Sam', 25)
my_dict = {'name': 'Sam', 'age': 25}

del my_var
del my_tuple
del my_dict

# Error: my_var is not defined
print(my_var)

# Error: my_tuple is not defined
print(my_tuple)

# Error: my_dict is not defined
print(my_dict)

# Ejemplo 3: eliminar elementos, sectores de una lista

# La deldeclaración se puede utilizar para eliminar un elemento en un índice determinado. Además, se puede utilizar para eliminar sectores de una lista.


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# deleting the third item
del my_list[2]

# Output: [1, 2, 4, 5, 6, 7, 8, 9]
print(my_list)

# deleting items from 2nd to 4th
del my_list[1:4]

# Output: [1, 6, 7, 8, 9]
print(my_list)

# deleting all elements
del my_list[:]

# Output: []
print(my_list)

# Ejemplo 4: eliminar un par clave: valor de un diccionario

person = { 'name': 'Sam',
  'age': 25,
  'profession': 'Programmer'
}

del person['profession']

# Output: {'name': 'Sam', 'age': 25}
print(person)

# No puede eliminar elementos de tuplas y cadenas. Es porque las tuplas y las cadenas son inmutables; objetos que no se pueden cambiar después de su creación.


my_tuple = (1, 2, 3)

# Error: 'tuple' object doesn't support item deletion
del my_tuple[1]

# Sin embargo, puede eliminar una tupla o una cadena completa.


my_tuple = (1, 2, 3)

# deleting tuple
del my_tuple