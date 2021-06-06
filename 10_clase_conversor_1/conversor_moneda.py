# #conversor de monedas

#pesos colombiano a dólares

pesos = input("¿cuántos pesos Colombianos tienes?: ") #input ingresa un valor
pesos = float(pesos)  #float convierte a deimal
valor_dolar = 3875  #valor del dólar
dolares = pesos / valor_dolar # 10 mil pesos entre 3875
dolares = round(dolares, 2)  #esto sirve para obtener apenas 2 decimales
dolares = str(dolares) #str convierte a texto
print("Tienes $" + dolares + " dólares")


#dólares a pesos Colombianos

dolares = input("¿cuántos dólares tienes?: ")
dolares = float(dolares)
valor_peso = 4000
pesos = dolares / valor_peso
pesos = round(dolares, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")

