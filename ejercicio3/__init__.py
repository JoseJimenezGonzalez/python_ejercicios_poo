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
with open(archivo_csv_destino, "w", newline="") as csvfile:

    writer = csv.writer(csvfile, delimiter=";")

    writer.writerow(["NOMBRE", "PRECIO", "CATEGORIA"])

    for fruta in frutas:
        writer.writerow([fruta["nombre"], fruta["precio"], fruta["categoria"]])