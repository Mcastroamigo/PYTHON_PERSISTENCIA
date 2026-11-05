#Al iniciar el programa se debe mostrar el siguiente menu: 
#1.- Añadir nota
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota media
#5.- Mostrar todas
#6.- Salir

#El usuario elige una opción (1 al 6) y el programa le muestra o le pide
#los datos necesarios para llevar a cabo ea acción. Despues, vuelve a salir el menú
#y así hasta que elija la opción de salir. 
#Las notas se guardan en un fichero 

"""
lista = []
contador = 0
suma_notas = 0
numero_notas = 0
opcion = 0

while opcion != 6:

    print("#1.- Añadir nota")
    print("#2.- Añadir notas extremas")
    print("#3.- Total de aprobados")
    print("#4.- Nota media")
    print("#5.- Mostrar todas")
    print("#6.- Salir")

    opcion = int(input("Introduce una opcion: "))

    if opcion == 1:
        
        nota=(input("introduce una nota: "))
        lista.append(nota)
        with open("notas.txt","a") as f:
            f.write(nota)
            print("nota añadida")    
        
        

    elif opcion == 2:
        with open("notas.txt", "r") as f:
        

            for linea in f:
                lista.append(float(linea.strip()))

            if len(lista) > 0:
                nota_mayor = float(max(lista))
                nota_menor = float(min(lista))

                print("Nota mayor:", nota_mayor)
                print("Nota menor:", nota_menor)

            else:
                print("No hay notas guardadas")

    elif opcion == 3:
        contador = 0
        
        with open("notas.txt","r") as f:
            lista = f.readlines()
            for aprobados in lista:
                aprobado = float(aprobados.strip())
                if aprobado >= 5:
                    contador += 1

                print("El numero de aprobados es:", contador)

    elif opcion == 4:
        suma_notas = 0
        
        with open("notas.txt","r") as f:
            lista = f.readlines()
            for notas in lista:
                suma_notas += notas

        numero_notas = len(lista)

        with open("notas.txt","r") as f:
            f.readlines()
            if numero_notas > 0:
                media = suma_notas / numero_notas
                print("La nota media es:", media)
            else:
                print("No hay notas para calcular la media")

    elif opcion == 5:
        with open("notas.txt","r") as f:
            linea=f.readlines()
            print(linea)
                  

    elif opcion == 6:
        print("Fin de programa")

    else:
        print("Opcion no valida")
"""

#Al iniciar el programa se debe mostrar el siguiente menú:
#1.- Añadir nota
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota media
#5.- Mostrar todas
#6.- Salir

#El usuario elige una opción (1 al 6) y el programa le muestra o le pide
#los datos necesarios para llevar a cabo ea acción. Despues, vuelve a salir el menú
#y así hasta que elija la opción de salir. 
#Las notas se guardan en un fichero
dir_fichero="notas.txt"
#funciones propias
def menu():
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")
def nueva_nota(nota):
    with open(dir_fichero,"a") as f:
        f.write(nota+"\n")
        
def aprobados():
    with open(dir_fichero,"r") as f:      
        aprobados=0
        linea=f.readline()
        while(linea!=""):
            if int(linea.strip())>=5:
                aprobados+=1
            linea=f.readline()
    return aprobados
def nota_baja():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    return min(notas,key=lambda n:int(n.strip()))
def nota_alta():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    return max(notas,key=lambda n:int(n.strip()))
def media():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    if not notas:
        return 0
    return sum([int(n.strip()) for n in notas])/len(notas)
def mostrar_notas():
    with open(dir_fichero,"r") as f:
        linea=f.readline()
        while linea!="":
            print(linea.strip())
            linea=f.readline()
#programa principal
opcion_elegida=0
while opcion_elegida!=6 :
    menu()
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            nueva_nota(input("Introduce nota "))
        case 2:
            print(f"nota más alta {nota_alta()}")
            print(f"nota más baja {nota_baja()}")
        case 3:
            print(f"total de aprobados {aprobados()}")
        case 4:
            print(f"La nota media es {media()}")
        case 5:
            mostrar_notas()
        case 6:
            print("Fin del programa!")
        case _:
            print("opción no válida")
            
    """
    #intento abrir el fichero como lectura y si no existe lo creamos
try:
    f=open(dir_fichero,"r")
    f.close()
except FileNotFoundError:
    f=open(dir_fichero,"w")
    f.close()
    
    """