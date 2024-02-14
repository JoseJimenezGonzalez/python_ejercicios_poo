from urllib import request
from json import loads


url_completa = "https://api.coindesk.com/v1/bpi/currentprice.json"
f = request.urlopen(url_completa)
datos_json = f.read().decode("utf-8")
datos_diccionario = loads(datos_json)

#Obtenemos la fecha
fecha = datos_diccionario['time']['updateduk']
print(fecha)

#Nos traemos cada objeto
for clave, valor in datos_diccionario['bpi'].items():
    codigo = valor['code']
    descripcion = valor['description']
    valor_numerico = valor['rate_float']
    print(f"Codigo: {codigo}, descripción: {descripcion} y equivale a : {valor_numerico} bitcoins.")
