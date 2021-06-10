#información tomada de https://www.programiz.com/python-programming/methods/list/extend


"""
El método extend () agrega todos los elementos de un iterable (lista, tupla, cadena, etc.) al final de la lista.

La sintaxis del extend()método es:

list1.extend (iterable)
Aquí, todos los elementos de iterable se agregan al final de list1.

extender () Parámetros
Como se mencionó, el extend()método toma un iterable como lista, tupla, cadena, etc.

Valor de retorno de extender ()
El extend()método modifica la lista original. No devuelve ningún valor.
"""



# Ejemplo 1: uso del método extend ()
# languages list
languages = ['French', 'English']

# another list of language
languages1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
languages.extend(languages1)

print('Languages List:', languages)

# Producción

# Lista de idiomas: ['francés', 'inglés', 'español', 'portugués']

# Ejemplo 2: agregar elementos de tupla y establecerlos en la lista
# languages list
languages = ['French']

# languages tuple
languages_tuple = ('Spanish', 'Portuguese')

# languages set
languages_set = {'Chinese', 'Japanese'}

# appending language_tuple elements to language
languages.extend(languages_tuple)

print('New Language List:', languages)

# appending language_set elements to language
languages.extend(languages_set)

print('Newer Languages List:', languages)

# Producción

# Lista de nuevos idiomas: ['francés', 'español', 'portugués']
# Lista de idiomas más nuevos: ['francés', 'español', 'portugués', 'japonés', 'chino']
# Otras formas de ampliar una lista

# También puede agregar todos los elementos de un iterable a la lista usando:

# 1. el operador +

a = [1, 2]
b = [3, 4]

a += b    # a = a + b

# Output: [1, 2, 3, 4]
print('a =', a)
Producción

a = [1, 2, 3, 4]

# 2. la sintaxis de división de listas

a = [1, 2]
b = [3, 4]

a[len(a):] = b

# Output: [1, 2, 3, 4]
print('a =', a)

# Producción

# a = [1, 2, 3, 4]
# Python extend () Vs append ()
# Si necesita agregar un elemento al final de una lista, puede usar el append()método.

a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

# a1 = [1, 2, 3, 4]
a1.extend(b) 
print(a1)

# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2)

# Producción

# [1, 2, 3, 4]
# [1, 2, (3, 4)]
# Para obtener más información, visite el método list append () .