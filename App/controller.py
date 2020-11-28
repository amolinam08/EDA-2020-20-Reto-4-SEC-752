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

import config as cf
from App import model
import csv
import os

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def init():

    ### Inicializa el catalogo###
    analyzer = model.newAnalyzer()
    return analyzer

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadFile(citiB,tripfile):
    tripfile = cf.data_dir + tripfile
    input_file = csv.DictReader(open(tripfile, encoding="utf-8"),delimiter=",")
    for trip in input_file:
        model.addTrip(citiB, trip)
    return citiB


def loadTrips(citiB):
    for filename in os.listdir(cf.data_dir):
        if filename.endswith('.csv'):
            print('Cargando archivo: ' + filename)
            loadFile(citiB, filename)
    return citiB

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def totalStations(analyzer):
    return model.totalStations(analyzer)


def totalTrips(analyzer):
    return model.totalTrips(analyzer)


def sameCC(sc, station_1, station_2):
    return model.sameCC(sc, station_1, station_2)


def connectedComponents(citiB):
    return model.connectedComponents(citiB)
    
def maxEnd(citiB):
    g = citiB
    return model.maxEnd(g)

def maxStart(citiB):
    g = citiB
    return model.maxStart(g)

def minStation(citiB):
    g = citiB
    return model.minStation(g)   

def RecRoutes(citiB, age):
    a = model.RecRoutes(citiB, age)
    print ('La estación mas concurrida por el grupo de edad seleccionada es la: ', a[0])
    print ('La estación a la que más llega gente del grupo de edad seleccionada es la: ', a[1])
    print ('La ruta entre esas estaciones es: ', a[2])

def interestRoute(citiB, lat1, lon1, lat2, lon2):

    a = model.interestRoute(citiB, lat1, lon1, lat2, lon2)
    print ('La estación más cercana a su punto de salida es la: ', a[0])
    print ('La estación más cercana a su destino es la: ', a[1])
    print ('La ruta entre las estaciones es: ', a[2])