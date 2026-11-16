import pandas as pd

""" A partir del fichero houses.csv

Se solicita un presupuesto y te muestra los datos
de los pisos que puedes comprar ordenados de mayor a menor precio """

df=pd.read_csv("viviendas.csv")

presupuesto=float(input("introduce presupuesto"))

print(f"")