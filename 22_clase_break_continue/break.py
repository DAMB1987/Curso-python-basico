#break

"""
i = es una variable standar en el ciclo por for por la comunidad, es buena práctica
==, doble igual significa igual a
explicación
range va de 0 a 9999
teniniendo la variable i, dispobible en cada vuelta del ciclo
se imprime la variable i en cada vuelta, pero si en algún momento i llegase a valer 5678, se corta el ciclo y no sé ejecuta más el ciclo
"""

# def run():    #función principal, run o main
#     for i in range(10000):
#         print(i)
#         if i == 5678:
#             break
# #result (1 a 9999) pero solo llega del 1 hasta 5678,dado que se establecio la variable i


# if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
#   run()


#string con break

"""
Explicación:
Estoy grabando el curso de  python
Est.
solo toma Est, por que antes de llegar a la o, break corta el ciclo
--------------------------------
mensaje: Estoy grabando un curso de python
si en letra == "p":, daria como resultado
Estoy grabando un curso de (se corta el ciclo antes de llegar a python)
"""

# def run():    #función principal, run o main
#     texto = input("Escribe un texto: ")
#     for letra in texto:
#       if letra == 'o':
#         break
#       print(letra)


# if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
#   run()


#ciclo while con break

def run():    #función principal, run o main
 contador = 0
while True:
    print(contador)
    contador += 1
    if contador > 10:
        print("Esto que es!")
        break


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()