import pandas as pd

def cm_a_pulgadas(cm):
    """Convierte centímetros a pulgadas."""
    return cm / 2.54

# Leer el archivo Excel con las medidas
df= pd.read_excel("mueble_medidas.xlsx")

# Añadir una columna al DataFrame con las medidas en pulgadas
df["Pulgadas:"] = df["Centimetros:"].apply(cm_a_pulgadas)

# Guardar el DataFrame actualizado en un nuevo archivo Excel
df.to_excel("mueble_medidas_convertidas.xlsx", index=False)

print("Conversión completada. El archivo mueble_medidas_convertidas.xlsx ha sido creado.")

# El Script que debo poner en consola para hacer la conversion y guardar en un nuevo archivo Excel.
# python .\nombre_el_archivo_desarrollado.py  en este caso particular seria python .\programa_conversor.py 

# Antes de ejecutar el programa debe asegurarse de tener instalado los paquetes necesarios:
# Puede instalarlo usando el archivo requerimientos.txt que contiene los paquetes necesarios:
# pip install -r .\requerimientos.txt



