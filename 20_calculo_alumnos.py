import pandas as pd


lista_alumnos=pd.read_json("alumnos.json")
    

print(f"nota media global: {lista_alumnos["nota"].mean():.2f}")
grupo=lista_alumnos.groupby("curso").agg(nota_mayor=("nota","max"),total_alumnos=("nombre","count"))
print(grupo)