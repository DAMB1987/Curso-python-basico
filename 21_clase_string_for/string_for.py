#string con for
#ctrl c, cierra la consola a la "fuerza"

"""
Recorrer una cadena de caracteres
y pasa por cada una de las estructuras
letra in nombre = imprime cada letra en el ciclo
letra = variable que representa cada uno de los caracteresen cada una de las repeticiones de nuestro ciclo for
¿de donde saca letra estos caracteres? sale de nombre, ya que "nombre" es un string
"""

# def run():    #función principal, run o main
#     nombre = input("Escribe tu nombre: ")
#     for letra in nombre:  #variable letra
#       #letra  = nombre.capitalize()  #.capitalize, sirve para poner la 1ra letra en D
#       print(letra)


# if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
#   run()

# siempre la variable que se use para in, esta variable siempre va ir en print

def run():    #función principal, run o main
  frase = input("Escribe una frase: ")
  for caracter in frase:
    print(caracter.upper())


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()




