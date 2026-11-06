
import math
import csv


coordenadas = []


def distancia(punto1, punto2):
    return math.hypot(punto1[0]-punto2[0], punto1[1]-punto2[1])

with open("coordenadas.csv", "r") as archivo:
    lector = csv.reader(archivo)
    

    next(lector)

    for fila in lector:
        x = int(fila[0])
        y = int(fila[1])

        coordenadas.append((x, y))


print(coordenadas)


pos_usuario = (int(input("Tu posición x: ")), int(input("Tu posición y: ")))


distancia_corta = distancia(coordenadas[0], pos_usuario)

coordenada_tienda = coordenadas[0]


for coord in coordenadas:


    dist = distancia(coord, pos_usuario)


    if dist < distancia_corta:
        distancia_corta = dist
        coordenada_tienda = coord


print(f"La tienda más cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}")


""" #SOLUCION PROFESOR
#Se pide al usuario su posición, después el programa
#le mostrará las coordenadas del punto 
#más cercano a su posición 
import math
import csv

def distancia(punto1,punto2):
   return math.dist(punto1,punto2)
   return math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1]) 

pos_usuario=(int(input("Tu posición x: ")),int(input("Tu posición y: ")))
dir_fichero="coordenadas.csv"
#En esta variable se obtendrá la distnacia más corta
distancia_corta=None
#En esta variable se deberá obtener la tupla de la tienda más cercana
coordenada_tienda=None
with open(dir_fichero,"r") as f:
    coordenadas=csv.DictReader(f)
    for row in coordenadas:
        coord=(int(row["x"]),int(row["y"]))
        if distancia_corta==None: #es la primera vez
            distancia_corta=distancia(coord,pos_usuario)
        if coordenada_tienda==None:
            coordenada_tienda=coord
        #recorremos las coordenadas y para cada una de ellas,
        #obtenemos la distancia con la posición del usuario. Si encontramos que esa distancia
        #es inferior distancia_corta, actualizamos tanto las variables distancia_corta
        #como coordenada_tienda
        dist=distancia(coord,pos_usuario)
        if dist<distancia_corta:
            distancia_corta,coordenada_tienda=dist,coord
print(f"La tienda mas cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}") """


#solucion profesor2

"""
with open(dir_fichero,"r") as f:
    next(f)
    coordenadas=list(csv.reader(f))
    coordenada_tienda=min(coordenadas,key=lambda c:distancia((int(c[0]),int(c[1])),pos_usuario))
print(f"La tienda mas cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}")

"""
