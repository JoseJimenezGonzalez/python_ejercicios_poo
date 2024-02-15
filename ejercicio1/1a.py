from urllib import request
from json import loads

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
f = request.urlopen(url)
datos_json = f.read().decode("utf-8")
datos_diccionario = loads(datos_json)

fecha = datos_diccionario['time']['updateduk']
print(fecha)

for clave, valor in datos_diccionario['bpi'].items():
    codigo = valor['code']
    descripcion = valor['description']
    equivalencia = valor['rate_float']
    print(f"Código: {codigo}, descripción: {descripcion} y 1 bitcoin equivale a: {equivalencia} {codigo}")


