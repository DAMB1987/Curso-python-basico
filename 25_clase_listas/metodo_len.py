#información tomada de https://www.programiz.com/python-programming/methods/built-in/len

"""
La función len () devuelve el número de elementos (longitud) de un objeto.


La sintaxis de len()es:

lente)
Parámetros len ()
s : una secuencia (cadena, bytes, tupla, lista o rango) o una colección (diccionario, conjunto o conjunto congelado)

Valor de retorno de len ()
len() La función devuelve el número de elementos de un objeto.

No pasar un argumento o pasar un argumento no válido generará una TypeErrorexcepción.

"""

# Ejemplo 1: ¿Cómo funciona len () con tuplas, listas y rango?

testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))

# Producción

# [] la longitud es 0
# [1, 2, 3] la longitud es 3
# (1, 2, 3) la longitud es 3
# La longitud del rango (1, 10) es 9

# Ejemplo 2: ¿Cómo funciona len () con cadenas y bytes?

testString = ''
print('Length of', testString, 'is', len(testString))

testString = 'Python'
print('Length of', testString, 'is', len(testString))

# byte object
testByte = b'Python'
print('Length of', testByte, 'is', len(testByte))

testList = [1, 2, 3]

# converting to bytes object
testByte = bytes(testList)
print('Length of', testByte, 'is', len(testByte))

# Producción

# La longitud de es 0
# La longitud de Python es 6
# La longitud de b'Python 'es 6
# La longitud de b '\ x01 \ x02 \ x03' es 3

# Ejemplo 3: ¿Cómo funciona len () con diccionarios y conjuntos?
testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))

# Empty Set
testSet = set()
print(testSet, 'length is', len(testSet))

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

testDict = {}
print(testDict, 'length is', len(testDict))

testSet = {1, 2}
# frozenSet
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))
# Producción

# {1, 2, 3} la longitud es 3
# set () length es 0
# {1: 'uno', 2: 'dos'} la longitud es 2
# {} la longitud es 0
# frozenset ({1, 2}) la longitud es 2
# Visite estas páginas para obtener más información sobre:

# Diccionario de Python
# Conjunto de Python
# Python congelado ()
# Internamente, len()llama al __len__método del objeto . Puedes pensar en len()como:

# def len (s):
#     return s .__ len __ ()
# Por lo tanto, puede asignar una longitud personalizada al objeto (si es necesario)

# Ejemplo 4: ¿Cómo funciona len () para objetos personalizados?
class Session:
    def __init__(self, number = 0):
      self.number = number
    
    def __len__(self):
      return self.number


# default length is 0
s1 = Session()
print(len(s1))

# giving custom length
s2 = Session(6)
print(len(s2))

# Producción

# 0
# 6