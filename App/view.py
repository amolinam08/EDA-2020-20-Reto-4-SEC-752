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

citiB1 = "201801-1-citibike-tripdata.csv"
#citiB2 = "201801-2-citibike-tripdata.csv"
#citiB3 = "201801-3-citibike-tripdata.csv"
#citiB4 = "201801-4-citibike-tripdata.csv"

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def print_menu():
    print("\n")
    print("Bienvenido")
    print("1- Inicializar Analizador.")
    print("2- Cargar información de bicicletas de Nueva York.")
    print("3- Cantidad de clusters de viajes.")
    print("4- Conocer rutas circulares.")
    print("5- Recomendador de rutas.")
    print("6- Ruta de interes turistico.")
    print("0- Salir.")

def Opt2():
    print("\nCargando información...")
    controller.loadTrips(cont. citiB1)
    num_edges = controller.totalConnections(cont)
    num_vertex = controller.totalStops(cont)
    print('Numero de vertices en el grafo es: ' + str(numvertex))
    print('Numero de arcos en el grafo es: ' + str(numedges))
  


def Opt3():
    print("Se verificara si las estaciones pertenecen al mismo cluster")
    stat1 = input("Ingrese el ID de la primera estación: ")
    stat2 = input("Ingrese el ID de la segunda estación: ")
    same = controller.sameCluster(cont, stat1,stat2)
    if same = True:
        same = "si"
    else:
        same ="no"
    print('Las estaciones '+same+" estan en el mismo cluster")
    
while True:
    printMenu()

    inputs = input('Seleccione una opción para continuar\n>')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()
    elif int(inputs[0]) == 2:
        executiontime = timeit.timeit(Opt2, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    elif int(inputs[0]) == 3:
        executiontime = timeit.timeit(Opt3, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    else:
        sys.exit(0)