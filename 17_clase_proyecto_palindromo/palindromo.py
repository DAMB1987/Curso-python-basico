#palindromo
#funcion principal que va a correr el programa al principio
#hacer que python corra linea por linea es una mala práctica
#siempre al iniciar un programa se debe crear una función como nosotros querramos poner, pero un standar es run o main, en la comunidad
#  pass #esto se usa para cuando todavia no se  escribe debajo del def o variable
#intrypoint es if _name_='_name_': , esto es el punto de entrada de un programa en python, cada vez que python se encuentra con if _name_='_name_': , empieza a correr todo lo que este por debajo, en este caso se usa run
#entre cada función dejar dos espacios ya que es buena práctica

# def run():
#     pass


# if __name__ == '__main__':
#     run()


def palindromo(palabra):
    palabra = palabra.replace(" ", " ")  #reemplaza todos los espacios con un string vacio o cadena vacia. luz azul, quedaria asi luzazul
    palabra = palabra.lower()  #lower poner letras en minusculas
    palabra_invertida = palabra[::-1] #[::-1], poner palabra al revés
    if palabra == palabra_invertida:
        return True
    else:
      return False


def run():
    palabra = input("Escribe una palabra : ")
    es_palindromo = palindromo(palabra) #palabra es un parametro
    if  es_palindromo == True:
      print("Es palindromo")
    else:
      print("No es palindromo")


if __name__ == "__main__":  #doble __
    run()
