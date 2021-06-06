#ciclo for

#Ejercicio imprimir del 1 al 1000

"""
for = para el
contador = variable
range = a una función, a la función range se le pueden pasar parametros es decir, quiero que inicie contador de 1 a 1000, se pone de esta manera.
in range(1, 1001)
in range = en el rango de 1000.

si se quiere llegar al número 1000, debemos poner 1001
"""

for contador in range(1, 1001):
    print(contador)

# #result 1 a 1000

"""
En este ejercicio se imprime la tabla del 11, 11 x 1, 11 x 2, etc, hasta llegar al número 9, razón en el range esta establecido hasta 10, siempre debe ser menor al valor para que se ejecute el ciclo.

i = variable
in range = en el rango que va de 0 a 9
print = que me imprima en cada vuelta del ciclo 11 x el valor de la variable i, en este caso de 0 a 9
"""

for i in range(10): #solo llega hasta el 9
  print(11 * i)


"""
Usando lista
"""
# a = list(range(1000))
# print(a)

