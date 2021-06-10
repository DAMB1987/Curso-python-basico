#información tomada de https://www.programiz.com/python-programming/methods/list/sort

"""
El método sort () ordena los elementos de una lista determinada en un orden ascendente o descendente específico.

La sintaxis del sort()método es:

list.sort (clave = ..., reverso = ...)
Alternativamente, también puede usar la función sorted () incorporada de Python para el mismo propósito.

ordenado (lista, clave = ..., reverso = ...)
Nota: La diferencia más simple entre sort()y sorted()es: sort()cambia la lista directamente y no devuelve ningún valor, mientras sorted()que no cambia la lista y devuelve la lista ordenada.

sort () Parámetros
De forma predeterminada, sort()no requiere ningún parámetro adicional. Sin embargo, tiene dos parámetros opcionales:

reverse : si True, la lista ordenada se invierte (o se ordena en orden descendente)
clave : función que sirve como clave para la comparación de clasificación
Valor de retorno de sort ()
El sort()método no devuelve ningún valor. Más bien, cambia la lista original.

Si desea que una función devuelva la lista ordenada en lugar de cambiar la lista original, utilice sorted().

"""

# Ejemplo 1: ordenar una lista dada
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)

# Producción

# Lista ordenada: ['a', 'e', ​​'i', 'o', 'u']
# Ordenar en orden descendente
# El sort()método acepta un reverseparámetro como argumento opcional.

# La configuración reverse = Trueordena la lista en orden descendente.

list.sort(reverse=True)

# Alternativamente sorted(), puede usar el siguiente código.

sorted(list, reverse=True)

# Ejemplo 2: ordenar la lista en orden descendente
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list (in Descending):', vowels)

# Producción

# Lista ordenada (en Descendente): ['u', 'o', 'i', 'e', ​​'a']
# Ordenar con función personalizada usando la tecla
# Si desea su propia implementación para ordenar, el sort()método también acepta una keyfunción como parámetro opcional.

# Según los resultados de la función clave, puede ordenar la lista dada.

list.sort(key=len)
# Alternativamente para ordenar:

sorted(list, key=len)

# Aquí, lenestá la función incorporada de Python para contar la longitud de un elemento.

# La lista se ordena según la longitud de cada elemento, desde el recuento más bajo hasta el más alto.

# Sabemos que una tupla se ordena utilizando su primer parámetro de forma predeterminada. Veamos cómo personalizar el sort()método para ordenar usando el segundo elemento.

# Ejemplo 3: ordenar la lista con la tecla
# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)

# Producción

# Lista ordenada: [(4, 1), (2, 2), (1, 3), (3, 4)]
# Tomemos otro ejemplo. Supongamos que tenemos una lista de información sobre los empleados de una oficina donde cada elemento es un diccionario.

# Podemos ordenar la lista de la siguiente manera:

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')
Producción

[{'Nombre': 'Alan Turing', 'edad': 25, 'salario': 10000}, {'Nombre': 'John Hopkins', 'edad': 18, 'salario': 1000}, {'Nombre ':' Mikhail Tal ',' edad ': 40,' salario ': 15000}, {' Nombre ':' Sharon Lin ',' edad ': 30,' salario ': 8000}]

[{'Nombre': 'John Hopkins', 'edad': 18, 'salario': 1000}, {'Nombre': 'Alan Turing', 'edad': 25, 'salario': 10000}, {'Nombre ':' Sharon Lin ',' edad ': 30,' salario ': 8000}, {' Nombre ':' Mikhail Tal ',' edad ': 40,' salario ': 15000}]

[{'Nombre': 'Mikhail Tal', 'edad': 40, 'salario': 15000}, {'Nombre': 'Alan Turing', 'edad': 25, 'salario': 10000}, {'Nombre ':' Sharon Lin ',' edad ': 30,' salario ': 8000}, {' Nombre ':' John Hopkins ',' edad ': 18,' salario ': 1000}]

# Aquí, para el primer caso, nuestra función personalizada devuelve el nombre de cada empleado. Dado que el nombre es a string, Python lo ordena por defecto usando el orden alfabético.

# Para el segundo caso, intse devuelve age ( ) y se ordena en orden ascendente.

# Para el tercer caso, la función devuelve el salario ( int) y se ordena en orden descendente utilizando reverse = True.

# Es una buena práctica utilizar la función lambda cuando la función se puede resumir en una línea. Entonces, también podemos escribir el programa anterior como:

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')

# Producción

# [{'Nombre': 'Alan Turing', 'edad': 25, 'salario': 10000}, {'Nombre': 'John Hopkins', 'edad': 18, 'salario': 1000}, {'Nombre ':' Mikhail Tal ',' edad ': 40,' salario ': 15000}, {' Nombre ':' Sharon Lin ',' edad ': 30,' salario ': 8000}]

# [{'Nombre': 'John Hopkins', 'edad': 18, 'salario': 1000}, {'Nombre': 'Alan Turing', 'edad': 25, 'salario': 10000}, {'Nombre ':' Sharon Lin ',' edad ': 30,' salario ': 8000}, {' Nombre ':' Mikhail Tal ',' edad ': 40,' salario ': 15000}]

# [{'Nombre': 'Mikhail Tal', 'edad': 40, 'salario': 15000}, {'Nombre': 'Alan Turing', 'edad': 25, 'salario': 10000}, {'Nombre ':' Sharon Lin ',' edad ': 30,' salario ': 8000}, {' Nombre ':' John Hopkins ',' edad ': 18,' salario ': 1000}]
# Para obtener más información sobre las funciones lambda, visite Python Lambda Functions .