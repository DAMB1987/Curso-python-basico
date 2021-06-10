#información tomada de https://www.programiz.com/python-programming/methods/string/count

"""
El método string count () devuelve el número de apariciones de una subcadena en la cadena dada.


En palabras simples, el count()método busca la subcadena en la cadena dada y devuelve cuántas veces la subcadena está presente en ella.

También toma parámetros opcionales comienzo y final para especificar las posiciones inicial y final en la cadena respectivamente.

La sintaxis del count()método es:

string.count (subcadena, inicio = ..., final = ...)
Parámetros de recuento de cadenas ()
count()El método solo requiere un único parámetro para su ejecución. Sin embargo, también tiene dos parámetros opcionales:

subcadena : cadena cuyo recuento se va a encontrar.
start (Opcional) : índice de inicio dentro de la cadena donde comienza la búsqueda.
end (Opcional) : índice final dentro de la cadena donde termina la búsqueda.
Nota: El índice en Python comienza desde 0, no 1.

Valor de retorno del recuento de cadenas ()
count() El método devuelve el número de apariciones de la subcadena en la cadena dada.

"""



# Ejemplo 1: contar el número de apariciones de una subcadena determinada
# define string
string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)
# Producción

# La cuenta es: 2
# Ejemplo 2: contar el número de apariciones de una subcadena determinada usando start y end
# define string
string = "Python is awesome, isn't it?"
substring = "i"

# count after first 'i' and before the last 'i'
count = string.count(substring, 8, 25)

# print count
print("The count is:", count)
# Producción

# El recuento es: 1
# Aquí, el recuento comienza después de que ise ha encontrado el primero , es decir, la 7thposición del índice.

# Y termina antes de la última i, es decir, la 25thposición de índice.