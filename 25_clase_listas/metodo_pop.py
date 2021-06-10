#información tomada de https://www.programiz.com/python-programming/methods/list/pop

"""
El método pop () elimina el elemento en el índice dado de la lista y devuelve el elemento eliminado.


La sintaxis del pop()método es:

list.pop (índice)
parámetros pop ()
El pop()método toma un solo argumento (índice).
El argumento pasado al método es opcional. Si no se pasa, el índice predeterminado -1 se pasa como argumento (índice del último elemento).
Si el índice pasado al método no está dentro del rango, arroja IndexError: el índice emergente fuera de rango .
Valor de retorno de pop ()
El pop()método devuelve el elemento presente en el índice dado. Este elemento también se elimina de la lista.

"""

# Ejemplo 1: elemento emergente en el índice dado de la lista

# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)

# Producción

# Valor devuelto: francés
# Lista actualizada: ['Python', 'Java', 'C ++', 'C']
# Nota: El índice en Python comienza desde 0, no 1.

# Si necesita hacer estallar la 4 ª elemento, lo necesario para pasar 3 al pop()método.

# Ejemplo 2: pop () sin índice y para índices negativos

# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:') 
print('Return Value:', languages.pop())
print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:') 
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:') 
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)

# Producción

# Cuando no se pasa el índice:
# Valor devuelto: C
# Lista actualizada: ['Python', 'Java', 'C ++', 'Ruby']

# Cuando se pasa -1:
# Valor de retorno: Ruby
# Lista actualizada: ['Python', 'Java', 'C ++']

# Cuando se pasa -3:
# Valor de retorno: Python
# Lista actualizada: ['Java', 'C ++']
# Si necesita eliminar el elemento dado de la lista, puede usar el método remove () .

# Y puede utilizar la deldeclaración para eliminar un elemento o sectores de la lista .