#metodos

nombre = input("¿cuál es tu nombre?: ")
nombre = nombre.upper()  #upper es un metodo, sirve para poner todas las letras en  Mayús
nombre = nombre.capitalize() #capitalize es un metodo, sirve para colocar la 1 letra en M
nombre = nombre.strip() #strip  sirve para eliminar espacios basura al principio o final
nombre = nombre.lower() #lower sirve para poner las letras en minusculas
nombre = nombre.replace("o", "a") #replace es una función que recibe parametros, que reemplaza el tipo de dato que se le ingrese, ejemplo diego pasaria a  doega
nombre[0]  #indice, esto representa un indice para acceder a casa letra de mi nombre
#razón por que se pone 0, en programación la mayoria de veces  toda letra o número empieza desde 0
#   0,  1, 2,  3,  4
#   d,  i, e,  g,  o

len(nombre) #lenes una función, sirve para saber cuántos caracteres tiene mi cadena
#Diego tiene 5 caracteres
len(letra)  #arrojaria 1, ya que es una letra
len("Hola! este es el curso de python") #tiene 32 caracteres

#en la consola al usar py, no se usa print, input, ya que dentro de py  viene integrada esto se llama la billind (funciones que se pueden invocar)
