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
import config
import collections
import time
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
from DISClib.Algorithms.Graphs import dfs
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import stack
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

def newAnalyzer():
    try:
        citiB = {}
        citiB["stations"] = m.newMap(numelements=1000,
                                    maptype="PROBING", 
                                    comparefunction=compareStations)
        citiB["graph"] = gr.newGraph(datastructure="ADJ_LIST",
                                    directed=True,
                                    size=1000,
                                    comparefunction=compareStations,)
        citiB["tripsInfo"] = lt.newList(datastructure="ARRAY_LIST")
        citiB["paths"] = None
        citiB["components"] = None
        return citiB
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')

# Funciones para agregar informacion al grafo

def addTrip(citiB, trip):
    start = trip['start station id']
    end = trip['end station id']
    initStation = trip['start station name']
    endStation = trip['end station name']
    duration = int(trip['tripduration']) 
    addStation(citiB, trip["start station id"])
    addStation(citiB, trip["end station id"])
    addAbS(citiB, start, end, duration)

def addStation(citiB, station_id):
    if not gr.containsVertex(citiB["graph"], station_id):
        gr.insertVertex(citiB["graph"], station_id)
    return citiB


def addAbS(citiB, start, end, duration):
    arc = gr.getEdge(citiB["graph"], start, end) 
    if arc is None:
        gr.addEdge(citiB["graph"], start, end, duration)
    return citiB



# ==============================
# Funciones de consulta
# ==============================

def totalStations(citiB):
    return gr.numVertices(citiB["graph"])

def totalTrips(citiB):
    return gr.numEdges(citiB["graph"])

def sameCC(sc, station_1, station_2):
    sct = scc.KosarajuSCC(sc["graph"])
    return scc.stronglyConnected(sct, station_1, station_2)

def connectedComponents(citiB):
    citiB["components"] = scc.KosarajuSCC(citiB["graph"])
    return scc.connectedComponents(citiB["components"])

def maxEnd(citiB):

    listVertex = gr.vertices(citiB["graph"])
    itr = it.newIterator(listVertex)
    dictstations = {}
    while it.hasNext(itr):
        station = it.next(itr)
        trips = gr.indegree(citiB["graph"], station)
        dictstations[station] = trips
    stations = idMax(dictstations)
    a1 = search(stations[0], citiB)
    a2 = search(stations[1], citiB)
    a3 = search(stations[2], citiB)
    a = [a1["name"], a2["name"], a3["name"]]
    return a
        

def maxStart(citiB):

    listVertex = gr.vertices(citiB["graph"])
    itr = it.newIterator(listVertex)
    dictstations = {}
    while it.hasNext(itr):
        station = it.next(itr)   
        trips = gr.outdegree(citiB["graph"], station)
        dictstations[station] = trips
    stations = idMax(dictstations)
    a1 = search(stations[0], citiB)
    a2 = search(stations[1], citiB)
    a3 = search(stations[2], citiB)
    a = [a1["name"], a2["name"], a3["name"]]
    return a

def minStation(citiB):

    listVertex = gr.vertices(citiB["graph"])
    itr = it.newIterator(listVertex)
    dictstations = {}
    while it.hasNext(itr):
        station = it.next(itr)  
        trips = gr.degree(citiB["graph"], station)
        dictstations[station]=trips
    stations = idLeast(dictstations)
    a1 = search(stations[0], citiB)
    a2 = search(stations[1], citiB)
    a3 = search(stations[2], citiB)
    a = [a1["name"], a2["name"], a3["name"]]
    return a

def RecRoutes(citiB, age):

    iterator = it.newIterator(m.keySet(citiB['stops']))
    start = 'Ninguna'
    maxOut = 0
    end = 'Ninguna'
    end2 = 'Ninguna'
    maxEnd = 0
    while it.hasNext(iterator):
        element = it.next(iterator)
        dicc = m.get(citiB['stops'],element)
        s = dicc['value'][2]
        arrival = dicc['value'][3]
        if s[categories(age)] > maxOut:
            max_salida = s[categories(age)]
            start = dicc['key']
        if arrival[categories(age)] > maxEnd:
            end2 = end
            maxEnd = arrival[categories(age)]
            end = dicc['key']
    if end == start:
        end = end2
    route = []
    dijsktra = djk.Dijkstra(citiB['graph'],str(start))
    if djk.hasPathTo(dijsktra, end):
        if djk.hasPathTo(dijsktra, end):
            routelt = djk.pathTo(dijsktra, end)
            iterator = it.newIterator(routelt)
            route.append(start)
            while it.hasNext(iterator):
                element = it.next(iterator)
                route.append(element['vertexB'])
    else:
        route = 'No hay ruta'
    return (start, end, route)

def interestRoutes(citiB, lat1, lon1, lat2, lon2)

    vertex = gr.vertices(citiB["connections"])
    iterator = it.newIterator(m.keySet(citiB['vertex']))
    start = []
    end = []
    while it.hasNext(iterator):
        element = it.next(iterator)
        locationp = m.get(analyzer["location"],element)
        location = me.getValue(locationp)

        dist1 = dist(lat1,location[0],lon1,location[1])
        dist2 = dist(lat2,location[0],lon2,location[1])
        
        try: 
            if start == []:
                start = (element,dist1)
            elif dist1 < start[1] or (dist1 <= start[1] and gr.outdegree(citiB["connections"],element)>gr.outdegree(citiB["connections"],start[1])):
                start = (element,dist1)   
        


# ==============================
# Funciones Helper
# ==============================

def search(id, citiB):

    mp = citiB['info']
    entry = m.get(mp, id)
    value = me.getValue(entry)
    return value

def idMax(dicc):

    list1 = list(dicc.values())
    list1.sort()
    max1 = list1[-1]
    max2 = list1[-2]
    max3 = list1[-3]
    list2 = []
    for i in dicc:
        if dicc[i] == max1 or dicc[i] == max2 or dicc[i] == max3 and dicc[i]:
            list2.append(i)
    a = [list2[0],list2[1],list2[2]] 
    return a 

def idLeast(dicc):

    list1 = list(dicc.values())
    list1.sort()
    max1 = list1[-1]
    max2 = list1[-2]
    max3 = list1[-3]
    list2 = []
    for i in dicc:
        if dicc[i] == max1 or dicc[i] == max2 or dicc[i] == max3 and dicc[i]:
            list2.append(i)
    a = [list2[0],list2[1],list2[2]] 
    return a


def categories(age):

    if age in range(0,11):
        key = '0-10'
    elif age in range(11,21):
        key = '11-20'
    elif age in range(21,31):
        key = '21-30'
    elif age in range(31,41):
        key = '31-40'
    elif age in range(41,51):
        key = '41-50'
    elif age in range(51,61):
        key = '51-60'
    else:
        key = '60+'

def dist(lat1, lat2, lon1, lon2):

    if type(lat1) == float and type(lon1) == float:
        lon1 = radians(lon1) 
        lon2 = radians(lon2) 
        lat1 = radians(lat1) 
        lat2 = radians(lat2)    
        dlon = lon2 - lon1  
        dlat = lat2 - lat1 
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        b = 2 * asin(sqrt(a))   
        c = 6371
        return round((b * c),2)
    else:
        return a 
# ==============================
# Funciones de Comparacion
# ==============================

def compareStations(s1, s2):
    s1 = int(s1)
    s2 = int(s2["key"])
    if s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    else:
        return -1