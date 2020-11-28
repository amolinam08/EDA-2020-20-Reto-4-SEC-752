"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import config as cf
import timeit
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________

citiB = "201801-1-citibike-tripdata.csv"
#citiB = "201801-2-citibike-tripdata.csv"
#citiB = "201801-3-citibike-tripdata.csv"
#citiB = "201801-4-citibike-tripdata.csv"

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n")
    print("Bienvenido")
    print("1- Inicializar Analizador.")
    print("2- Cargar información de CitiBike")
    print("3- Cantidad de clusters de viajes.")
    print("4- Conocer estaciones criticas.")
    print("5- Recomendador de rutas.")
    print("6- Ruta de interes turistico.")
    print("0- Salir.")

def Opt2():

    print("\nCargando información...")
    controller.loadFile(citiB,tripfile)
    num_edges = controller.totalTrips(cont)
    num_vertex = controller.totalStations(cont)
    print('Numero de vertices en el grafo es: ' + str(numvertex))
    print('Numero de arcos en el grafo es: ' + str(numedges))
    print("El limite de recursion actual: " + str(sys.getrecursionlimit()))
    sys.setrecursionlimit(recursionLimit)
    print("El limite de recursion se ajusta a: " + str(recursionLimit))
  


def Opt3():

    starting_station = input('\nID primera estación: ')
    ending_station = input('ID segunda estación: ')
    print('El número de componentes conectados es: ' + str(controller.connectedComponents(cont)))
    sc = controller.sameCC(cont, starting_station, ending_station)
    if (sc == True):
        print('Las estaciones ' + starting_station +' y ' + ending_station + ' pertenecen al mismo cluster')
    else:
        print('Las estaciones ' + ending_station  +' y ' + starting_station + ' no pertenecen al mismo cluster')
    

def Opt4():

    end = controller.maxendstation(cont)
    start = controller.maxstartstation(cont)
    Min = controller.minstation(cont)
    print("Los nombres de las 3 estaciones Top de llegada son: " + str(end))
    print("Los nombres de las 3 estaciones Top de salida son: " + str(start))
    print("Los nombres de las 3 estaciones menos utilizadas son: " + str(Min))

def Opt5():

    age = int(input('Edad del usuario: '))
    controller.RecRoutes(cont, age)

def Opt6():

    lat1 = float(input('Ingrese la latitud del punto de salida: '))
    lon1 = float(input('Ingrese la longitud del punto de salida: '))
    lat2 = float(input('Ingrese la latitud del punto de llegada: '))
    lon2 = float(input('Ingrese la longitud del punto de llegada: '))
    controller.interestRoute(cont, lat1, lon1, lat2, lon2)


while True:
    printMenu()

    inputs = input('Seleccione una opción para continuar\n>')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()
    elif int(inputs[0]) == 2:
        Opt2()
    elif int(inputs[0]) == 3:
        Opt3()
    elif int(inputs[0]) == 4:
        Opt4()
    elif int(inputs[0]) == 5:
        Opt5()
    elif int(inputs[0]) == 6:
        Opt6()
    else:
        sys.exit(0)