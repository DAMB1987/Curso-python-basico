#se podria usar menu para el ejercicio, tipo_pesos es un parametro
#Nota: siempre poner nuestras funciones por encima de nuestro código

def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿cuántos pesos " + tipo_pesos + "tienes?: ") #input ingresa un valor
    pesos = float(pesos)  #float convierte a decimal   #valor del dólar
    dolares = pesos / valor_dolar # 10 mil pesos entre 3875
    dolares = round(dolares, 2)  #esto sirve para obtener apenas 2 decimales
    dolares = str(dolares) #str convierte a texto
    print("Tienes $" + dolares + " dólares")

menu = """
Bienevenido al conversor de monedas 💰

1 -pesos colombianos☕
2 -pesos argentionos🥩
3 -pesos mexicanos  🌮

Elige una opción: """

opcion = int(input(menu))

#tipo_pesos = colombianos, argentino o mexicanos
#valor_dolar = 3785, 65, 24

if opcion ==1:
    conversor("colombianos", 3785) #entre comillas por que se imprime en la consola
elif opcion ==2:
      conversor("argentinos", 65)
elif opcion ==3:
      conversor("mexicanos", 24)
else:
  print("Elige una opción correcta por favor")