import pandas as pd
import matplotlib.pyplot as plt
# primero importo las librerias (pandas para trabajar con tablas y matplot para hacer graficos)
df = pd.read_csv("datos/sales_sample_2024.csv")

ventas_totales = df["sales_amount"].sum()

print(f"Ventas totales: {ventas_totales}")

df["sales_date"] = pd.to_datetime(df["sales_date"])
# to_datetime transforma el texto en la columna "sales_date" a "formato fecha" para que python pueda usarlo asi

df["mes"] = df["sales_date"].dt.month
# con .dt.month saco de la columna "sales_date" el dato del mes para usarlo despues

ventas_por_mes = df.groupby("mes")["sales_amount"].sum()
print()
print("Ventas por mes:")
print(ventas_por_mes.to_string())# aca le agregue el .to_string por que pandas le agrega un informe de la columna y el tipo de dato y no me gusta como se ve
ventas_por_mes.to_csv("resultados/ventas_por_mes.csv")
# agrupo las columnas por mes y sumo las ventas de cada mes y guardo la tabla en un achivo .csv

promedio_por_mes = df.groupby("mes")["sales_amount"].mean().round(1)# le agregue un round al final por que me quedaba con muchas comas
print()
print("Promedio de ventas por mes:")
print(promedio_por_mes.to_string())

promedio_por_mes.to_csv("resultados/promedio_ventas_por_mes.csv")
# .mean es para sacar el promedio de ventas mensual y tambien lo guardo en un archivo .csv

# sector grafico:

ventas_por_mes.plot(kind="bar")
# con esto  dibujo el grafico y le digo que sea de tipo barras
plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto vendido")
# le agrego referencias al grafico y lo guardo en un archivo png
plt.savefig("resultados/grafico_ventas_por_mes.png")