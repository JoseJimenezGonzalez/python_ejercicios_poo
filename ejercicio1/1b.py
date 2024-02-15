from urllib import request
from json import loads

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
f = request.urlopen(url)
datos_json = f.read().decode("utf-8")
datos_diccionario = loads(datos_json)['bpi']

moneda_usuario = input("Introduce DOLARES, EUROS ó LIBRAS")

if(moneda_usuario.upper() == "DOLARES"):
    codigo = "USD"
elif(moneda_usuario.upper() == "EUROS"):
    codigo = "EUR"
elif(moneda_usuario.upper() == "LIBRAS"):
    codigo = "GBP"
else:
    codigo = ""
if(codigo == ""):
    print("No has introducido una moneda correcta")
else:
    cantidad_bitcoins = float(input("Introduce cantidad de bitcoins"))
    equivalencia = datos_diccionario[codigo]['rate_float']
    cantidad_equivalente = equivalencia * cantidad_bitcoins
    print(f"{cantidad_bitcoins} bitcoins equivalen a {cantidad_equivalente} de {moneda_usuario}")



