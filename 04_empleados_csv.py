import csv
"""
with open("empleados.csv","r") as f:
    datos=csv.reader(f,delimiter=",")
    for row in datos:
        print(row)
        
with open("empleados.csv","r") as f:
    datos=csv.DictReader(f)
    for row in datos:
        print(row)

with open("empleados.csv","r") as f:
    datos=list(csv.reader(f))
    print(datos)
    
with open("empleados.csv","r") as f:
    datos=list(csv.DictReader(f))
    print(datos)
""" 
"""   
#solicita la introduccion de un departamento y te muestra los nombre de las personas de ese departamento

departamento=input("introduce un departamento:")

with open("empleados.csv","r") as f:
    datos=csv.DictReader.split(f)
    for emp in datos:
        if emp["departamento"]==dep:
            print(emp["empleado"])
"""

#nombre del empleado con mayor salario

with open("empleados.csv", "r") as f:
    datos = list(csv.DictReader(f))

empleado_max=max(datos, key=lambda e:e["salario"])
print(f"El empleado con mayor salario es {empleado}")
print(f"Su salario es {mayor_salario}")

        
        

    