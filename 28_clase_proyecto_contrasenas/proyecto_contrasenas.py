#Generador de contrasenas

"""
lista unica

    caracteres = mayusculas + minusculas + simbolos +numeros
    choice, función especial del modulo random
    .choice(caracteres)
    elijo un caracter al azar, y se guarda dentro de la variable caracter_random
"""

#similitud al navegador firefox

import random

def generar_contrasena():
      mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
      minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
      simbolos =["!","#", "$", "%" ,"&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\ ","/", "]", "^", "_","`", "{", "|", "}", "~"]
      numeros = ["1","2","3","4","5","6","7","8","9","0"]

      caracteres = mayusculas + minusculas + simbolos + numeros

      contrasena  = ["A","b","#","u","@","o","&","F","(","T","z","<","k","H","j","0","%",",","*"]

      for i in range(15):  #va a tener 15 caracteres para las vueltas del ciclo
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)     #lista contrasena


      contrasena = "".join(contrasena) #convertir lista en un string, usar comillas simples
      return contrasena


def run():    #función principal, run o main
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
    run()

