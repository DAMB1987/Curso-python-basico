#información tomada de https://www.programiz.com/python-programming/methods/list/index

"""
El método index () devuelve el índice del elemento especificado en la lista.

La sintaxis del index()método de lista es:

list.index (elemento, inicio, fin)
list index () parámetros
El index()método de lista puede tomar un máximo de tres argumentos:

elemento : el elemento que se va a buscar
start (opcional): comienza a buscar desde este índice
end (opcional): busca el elemento hasta este índice
Valor devuelto del índice de lista ()
El index()método devuelve el índice del elemento dado en la lista.
Si no se encuentra el elemento, se genera una ValueErrorexcepción.
Nota: El index()método solo devuelve la primera aparición del elemento coincidente.

"""

# Ejemplo 1: encontrar el índice del elemento
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print('The index of i:', index)
# Producción

# El índice de e: 1
# El índice de i: 2

# Ejemplo 2: índice del elemento que no está presente en la lista
# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# index of'p' is vowels
index = vowels.index('p')
print('The index of p:', index)

# Producción

# ValueError: 'p' no está en la lista

# Ejemplo 3: Trabajo de index () con parámetros de inicio y fin

# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'i' in alphabets
index = alphabets.index('e')   # 1
print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
index = alphabets.index('i', 3, 5)   # Error!
print('The index of i:', index)

# Producción

# El índice de e: 1
# El índice de i: 6
# Rastreo (llamadas recientes más última):
#   Archivo "* lt; cadena>", línea 13, en 
# ValueError: 'i' no está en la lista