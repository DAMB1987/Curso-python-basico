#Proyecto videojuego

"""
Juego advina el número
Reglas:
- la computadora v aa pensar un número aleatorio entre el 1 al 100
- Nosotros pensar que número advino la computadora
-Si acertamos la computadora mostrará un mensaje "Ganaste"
-Si nosotrosfallamos la computadora mostrará un mensaje "El número que esta buscando es más grande"
"el número que estás buscando es más pequeño "
"""

"""
¿comó hacer que la computadora piense un número aleatorio del 1 al 100?
se debe usar un modulo de python
modulo es un paquete de código, escrito por las personas que crearon python, que nosotros tenemos disponible para ejecutar funciones escritas por esas personas, que hacen el trabajo por nosotros

Usamos:
import random (modulo random es el paquetede código que contiene funciones para trabajar con la aleatoriedad del lenguaje )

random.
con el . , nosotros accedemos a la funcionesde un determinado modulo
randint()
genera un número aleatorio entero, que va de un número a y a un número b
número inicial es 1 hasta el 100

Por parte del usuario (nosotros)
numero_elegido
la función input = texto
la función int = número entero
! = es distinto
if numero_elegido < numero_aleatorio:
si el número _elegido es menor a numero_aleatorio
recibe este mensaje
 print("Busca un número más grande")
 sino, recibe como mensaje Busca un número más pequeño
 else:
        print("Busca un número más pequeño")
Oportunidad de ingresar un nuevo número
 numero_elegido = int(input("Elige otro número: "))

 ¡Nota!: el  numero_elegido = int(input("Elige otro número: ")) debe ir a la misma altura que el if, sino ocaciona un bucle infinito

 Si acierta recibe este mensaje
  print("¡Ganaste!")
"""

import random

def run():    #función principal, run o main
    numero_aleatorio  = random.randint(1, 100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
      if numero_elegido < numero_aleatorio:
        print("Busca un número más grande")
      else:
        print("Busca un número más pequeño")
      numero_elegido = int(input("Elige otro número: "))  #ver nota
    print("¡Ganaste!")


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()