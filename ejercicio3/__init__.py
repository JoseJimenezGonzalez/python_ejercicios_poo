import csv

frutas = [
    {
        "nombre":"Manzana",
        "precio":2.4,
        "categoria":"A"
    },
    {
        "nombre":"Peras",
        "precio":1.3,
        "categoria":"B"
    },
    {
        "nombre":"Naranjas",
        "precio":4.4,
        "categoria":"C"
    }
]

archivo_csv_destino = "frutas.csv"
with open(archivo_csv_destino, mode='w', newline='') as file:
    # Definir los encabezados en mayúsculas y separados por ;
    encabezados = frutas[0].keys()
    # Crear un escritor de CSV
    escritor_csv = csv.DictWriter(file, fieldnames=encabezados, delimiter=';')
    # Escribir los encabezados en el archivo
    escritor_csv.writeheader()
    #Escribir las filas en el archivo
    for fruta in frutas:
        escritor_csv.writerow(fruta)
print(f"El archivo '{archivo_csv_destino}' ha sido creado con éxito.")