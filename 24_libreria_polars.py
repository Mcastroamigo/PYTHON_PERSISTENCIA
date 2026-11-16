import polars as pl

"""
    Porqué polars?
    1- Estilo y metodos mas modernos
    2- Mas eficiente
"""
datos = [ 
    {"nombre": "Ana", "edad": 25, "salario": 25000,"departamento":"ventas"}, 
    {"nombre": "Luis", "edad": 32, "salario": 32000,"departamento":"informática"}, 
    {"nombre": "Marta", "edad": 28, "salario": 28000,"departamento":"informática"}, 
    {"nombre": "Pedro", "edad": 41, "salario": 41000,"departamento":"ventas"} 
]

df = pl.DataFrame(datos) 
print(df)

#Acesso a filas y columnas
print(df["edad"].to_list()) #columna lista de valores
print(df.row(0,named=True)) #Diccionario con los datos de la fila
print(df.to_dicts()) #convierte todo el dataframe en un diccionario

#filtrado
print(df.filter(pl.col("salario")>30000))
print(df.filter(pl.col("salario")>30000&pl.col("edad")<50))

#ordenacion
print(df.sort(by="edad",descending=False))
print(df.sort(by="salario",descending=True).row(0)[0]) #se wueda con la primera fila, y de eesta, con el primer elemento

#funciones para calculos min(),max(),mean(),count(),unique()
print("salario mas alto",df["salario"].max())
print("edad mas baja",df["edad"].min())

#seleccion
resultado = df.select(pl.col("salario").mean().alias("salario medio"),pl.col("edad").mean().alias("media edad"))
print(resultado)

print(df["departamento"].unique().to_list()) #muestra lista de departamentos sin duplicados

#agrupacion de un dataframe
print(df.group_by("departamento").agg(pl.col("salario").mean().alias("salario medio"),
                                pl.col("nombre").count().alias("total empleados")))

#recorrido de un dataframe
for element in df.iter_rows(named=True): #
    print(element)


