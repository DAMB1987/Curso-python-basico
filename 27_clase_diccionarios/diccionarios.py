#Diccionarios

"""
diccionario usa {}
un diccionario es una estructura de datos de llaves y valores
la diferencia con las listas no accedemos a un elemento a través de su indice, sino que se accede por medio de sus llaves
en diccionario podemos ponerle nombre al indice
el nombre de este indice se llama llave {}
los valores del diccionario se llaman valores
"""

#diccionario_1

def run():    #función principal, run o main
  mi_diccionario = {
      "llave1":1,
      "llave2":2,
      "llave3":3,
    }
  print(mi_diccionario)
  #results
  #{'llave1': 1, 'llave2': 2, 'llave3': 3}


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()


  """
  ¿Comó acceder a cada uno de los elementos?
  print(mi_diccionario["llave1"])
  print(mi_diccionario["llave2"])
  print(mi_diccionario["llave3"])
  """

#diccionario_2

def run():    #función principal, run o main
  mi_diccionario = {
      "llave1":1,
      "llave2":2,
      "llave3":3,
    }

  print(mi_diccionario["llave1"])
  print(mi_diccionario["llave2"])
  print(mi_diccionario["llave3"])

  #results
#   {'llave1': 1, 'llave2': 2, 'llave3': 3}
# 1
# 2
# 3


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()

#diccionario_3

def run():    #función principal, run o main
  mi_diccionario = {
      "llave1":1,
      "llave2":2,
      "llave3":3,
    }
poblacion_paises = {
  "Argentina":44938712,
  "Brasil": 210147125,
  "Colombia":50372424 ,
  }

print(poblacion_paises["Argentina"])
print(poblacion_paises["Brasil"])
print(poblacion_paises["Colombia"])


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()

"""
Recorrer diccionarios a partir de los valores de las  llaves
.keys(): (Argentina, Brasil, Colombia)

Recorrer diccionarios a partir de los valores del diccionario
.values
"""
def run():    #función principal, run o main

  poblacion_paises = {
    "Argentina":44938712,
    "Brasil": 210147125,
    "Colombia":50372424 ,
    }

  # for pais in poblacion_paises.keys():  #.keys(Argentina, Brasil, Colombia)
  #     print(pais)

  for pais in poblacion_paises.values():  #values(44938712,210147125,50372424)
      print(pais)


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()

#results .keys
#Argentina
# Brasil
# Colombia

#results .values
# 44938712
# 210147125
# 50372424

"""
¿comó mostrar dos valores de un diccionario
.tems
poblacion es un número entero
"""
def run():    #función principal, run o main

  poblacion_paises = {
    "Argentina":44938712,
    "Brasil": 210147125,
    "Colombia":50372424 ,
    }

  # for pais in poblacion_paises.keys():  #.keys(Argentina, Brasil, Colombia)
  #     print(pais)

  for pais, poblacion in poblacion_paises.items():  #.items, devuelve los dos valores
      print(pais +  " tiene"  +str(poblacion) +  " habitantes")


if __name__ == '__main__':  #entry point (punto de entrada) de un programa de python
  run()

#results
# Argentina tiene 44938712 habitantes
# Brasil tiene 210147125 habitantes
# Colombia tiene 50372424 habitantes