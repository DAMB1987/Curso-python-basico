#Proyecto prueba  primalidad

"""
caracteristica de los números primos todo número que se pueda dividir solamente por si mismo y por 1


numero es la variable
if es_primo(numero), es otra forma de escribir, porque se usa dos veces la variable numero y se entiende que es True
if es_primo == True
(1, numero + 1):  #el +1 se pude interpretar 1 a 10, range solo llega hasta el 9, pero como pone +1, ahora llega hasta el 10

 if i == 1 or i == numero:
 si i es igual a 1 or y si i es igual a numero
  continue
 vamos a continuar (continue), se salta una vuelta al ciclo
  if numero % i ==0:
  (% es dividir)
  si el numero modulo i nos da como resto == 0
 contador += 1 (contador = contador +1)
 se le suma un valor a contador
  if contador == 0:
  si contador es igual a 0
  return
  voy a tener un retorno verdadero
  else:
  return False
  sino vamos a obtener un retorno falso
"""

def es_primo(numero):
  contador = 0

  for i in range(1, numero + 1):
      if i == 1 or i == numero:
        continue
      if numero % i == 0:
        contador += 1 #contador = contador +1
  if contador == 0:
    return True
  else:
    return False


def run():    #función principal, run o main
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print("Es primo")
    else:
         print("No es primo")


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()



