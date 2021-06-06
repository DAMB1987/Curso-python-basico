menu = """
Bienevenido al conversor de monedas 💰

1 -pesos colombianos☕
2 -pesos argentionos🥩
3 -pesos mexicanos  🌮

Elige una opción: """

opcion = int(input(menu))

if opcion ==1:
  pesos = input("¿cuántos pesos Colombianos tienes?: ") #input ingresa un valor
  pesos = float(pesos)  #float convierte a deimal
  valor_dolar = 3875    #valor del dólar
  dolares = pesos / valor_dolar # 10 mil pesos entre 3875
  dolares = round(dolares, 2)  #esto sirve para obtener apenas 2 decimales
  dolares = str(dolares) #str convierte a texto
  print("Tienes $" + dolares + " dólares")
elif opcion ==2:
  pesos = input("¿cuántos pesos Argentinos tienes?: ") #input ingresa un valor
  pesos = float(pesos)  #float convierte a deimal
  valor_dolar = 65   #valor del dólar
  dolares = pesos / valor_dolar # 10 mil pesos entre 3875
  dolares = round(dolares, 2)  #esto sirve para obtener apenas 2 decimales
  dolares = str(dolares) #str convierte a texto
  print("Tienes $" + dolares + " dólares")
elif opcion ==3:
  pesos = input("¿cuántos pesos Mexicanos tienes?: ") #input ingresa un valor
  pesos = float(pesos)  #float convierte a deimal
  valor_dolar = 24   #valor del dólar
  dolares = pesos / valor_dolar # 10 mil pesos entre 3875
  dolares = round(dolares, 2)  #esto sirve para obtener apenas 2 decimales
  dolares = str(dolares) #str convierte a texto
  print("Tienes $" + dolares + " dólares")
else:
  print("Elige una opción correcta por favor")

