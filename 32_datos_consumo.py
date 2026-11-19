import numpy as np
consumos=[1250, 1380, 980, 1450, 1520, 1100, 1600]
dias=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


#1. Consumo total semanal
#2. Consumo medio diario
#3. Dias con mayor y menor consumo
#4. Días con consumo superior a la media

#6. Días con consumo un 20% inferior a la media
#7. Coste total, sabiendo que de lunes a viernes el coste del Kw es de 0,02 y en fin de semana del 0,018

consumos= np.array(consumos)
dias= np.array(dias)

total = np.sum(consumos)
print("Consumo total semanal: ", total)

media = np.mean(consumos)
print("Consumo medio diario: ", media)

dia_max = dias[np.argmax(consumos)]
dia_min = dias[np.argmin(consumos)]
dia_medio = dias[consumos > media]

print("Día con mayor consumo: ", dia_max)
print("Día con menor consumo: ", dia_min)
print("Día con consumo superior a la media: ", dia_medio)

# 7. Coste total (Lunes-Viernes: 0,02 | Fin de semana: 0,018)
tarifas = np.array([0.02, 0.02, 0.02, 0.02, 0.02, 0.018, 0.018])
coste_total = np.sum(consumos * tarifas)
print(f"7. Coste total semanal: {coste_total:.2f} €")