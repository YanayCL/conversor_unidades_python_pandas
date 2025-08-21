import pandas as pd # pd es una abreviatura común para pandas

# Dataframe es la informacion basica con el nombre de las piezas y centimetros para poder armar el Excel`

data = {
    "Piezas:": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros:": [50, 100, 75, 60, 80]
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel

df.to_excel("mueble_medidas.xlsx", index=False)

# Vamos a la carpeta donde esta el archivo .py, abrimos una consola y ponemos el comando:
# python creador_excel.py
# Esto creara un archivo llamado mueble_medidas.xlsx en la misma carpeta
# Asegurate de tener instalado el paquete openpyxl para poder crear archivos Excel

# Para crear un CSV en lugar de un Excel, puedes usar el siguiente comando:
# df.to_csv("mueble_medidas.csv", index=False)
# Esto creara un archivo llamado mueble_medidas.csv en la misma carpeta
# Con el mismo comando que utilice antes en consola para crear el excel 
# los archivos CSV son mas ligeros y pueden ser abiertos con Excel, Google Sheets 
# no tienen formato de celdas, 
# separan los datos por coma y no entienen las tildes
# y no permiten formulas, por lo que es mejor usar Excel si necesitas esas funcionalidades.