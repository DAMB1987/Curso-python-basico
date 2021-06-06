# continue

"""
se van a imprimir los números pares
% modulo
% 2 = dividido en 2
todos los números pares % 2, da 0
!= 0, es distinto
explicación:
si contador al dividirlo por 2, el resto de la división es distinto a 0, se salta la vuelta del ciclo, lo que esta debajo de continue no se va a ejecutar
ejemplo
solo va a imprimir, 2,4,6 etc ¿porqué?
continue toma el 0, 2, salta el número 3 y toma el 4, va de 2 en 2
"""

def run():    #función principal, run o main
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()



#while con continue

def run():    #función principal, run o main
  contatore = 0
while contatore < 10:
    contatore += 1
    if contatore == 3:
        print("saltato")
        continue
    print(contatore)


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()