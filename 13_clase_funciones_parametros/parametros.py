#parametros

#parametros son variables disponibles para usarlas dentro de la función

# def conversacion(mensaje):
#     print("Hola")
#     print("¿cómo estás?")
#     print(mensaje) #variable mensaje, Elegiste la opción 1,2,3
#     print("Adiós")

# opcion = int(input("Elige una opción(1,2,3): "))
# if opcion == 1:
#    conversacion("Elegiste la opcion   1")
# elif opcion == 2:
#     conversacion("Elegiste la opcion  2")
# elif opcion == 3:
#     conversacion("Elegiste la opcion  3")
# else:
#   print("Escoge la opción correcta")

  #result
  #Elige una opción(1,2,3): 1
# Hola
# ¿cómo estás?
# Elegiste la opcion   1
# Adiós

def suma(a, b):
    print("se suman dos números")
    resultado = a + b
    return resultado  #retorna resultado

sumatoria = suma(1, 4) #sumatoria se vuelve una variable iterante
print(sumatoria)