#while, mientras

#Ejercicio:
# imprimir todas las potencias de 2, dos al cuadrado,dos al cubo, dos a la cuarta,  hasta llegar al número mil

""""
al crear una variable constante, es decir que su valor no va a cambiar se escribe esa variable en mayúsculas, en este caso LIMITE

 contador es una variable que si cambia, se pone 0, porque va aumentando para aumentar a dos o tantas veces el contador lo diga, si el contador es = 3, va a multiplicar dos x dos que es igual a 2 al cubo

 (variable) potencia_2 (potencia de dos) = 2 elevado a contador
 #Todo número elevado a la 0, en matematicas es = a 1, excepto el 0

  while potencia_2  < LIMITE: #mientras la potencia_2 sea menor a LIMITE se va a ejecutar lo que esta debajo, cuando esta condición finalmente no se cumpla se termina el ciclo y ya no se ejecuta más

 ¿qué es lo que se va a ejecutar? print("2 elevado a " + str(constador) + " es igual a: " + str(2**constador))

 En el ciclo while, jamás se puede dejar un ciclo infinito, infinite loops
 LIMITE puede ser 1000, 1000000, el valor que uno le ponga, pero el while solo llega antes de 1000 o antes de 1000000, no superaran el limite porque ter termina el ciclo
 """

def run():    #función principal, run o main
    LIMITE  =1000 #LIMITE es una constante

    contador = 0   #contador es una variable que si cambia
    potencia_2 = 2**contador
    #definir el ciclo
    while potencia_2  < LIMITE: #mientras la condición se cumpla el ciclo se ejecuta
      print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))  #esto es lo que se ejecuta
      contador += 1   #contador = contador +1, esto sirve para deterner el ciclo
      potencia_2 = 2**contador


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
    run()

#results
#2 elevado a 0 es igual a: 1
# 2 elevado a 1 es igual a: 2
# 2 elevado a 2 es igual a: 4
# 2 elevado a 3 es igual a: 8
# 2 elevado a 4 es igual a: 16
# 2 elevado a 5 es igual a: 32
# 2 elevado a 6 es igual a: 64
# 2 elevado a 7 es igual a: 128
# 2 elevado a 8 es igual a: 256
# 2 elevado a 9 es igual a: 512


"""
explicación de como se ejecuta este ciclo
1)se llega al entry point, if __name__ == '__main__':
2)python encuentra la linea y ejecuta run
3) en la función run, va a definir una constante llamada LIMITE que va a tener el valor 1000
4) se define una variable llamada contador que tiene un valor a 0
5) se define otra variable llamada pontencia_2 = 2**contador
6)(minteras) while potencia_2  < LIMITE:, se ejecuta código
7) código que se ejecuta repetidamente hasta que deje de cumplirse, es el siguiente:
print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))
¿como se imprime esto?
se imprime 2 elevado a 0 = 1
ahora contador vale 1
potencia de 2 vale 2 elevado a 1 es = a 2
8) este ciclo se incrementa de 2 en 2  hasta llegar antes de 1000
9) si pasa más de 1000, el ciclo deja de ejecutarse
10) si sale typeError: can only concatenate str(not "int") to str, quiere decir no se puede concatenar un número con un string
solución
convertir pontencia_2 en un string, +  str(pontencia_2)
"""

#ejercicio imprimir del 1 al 1000

contador =  1
print(contador)
while contador < 1000:
  contador += 1 #contador = contador + 1
  print(contador)