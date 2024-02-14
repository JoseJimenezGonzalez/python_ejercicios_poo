from urllib import request
from json import loads

tipo_moneda = input("Introduce tipo de moneda que puede ser: DOLARES, EUROS ó LIBRAS")
cantidad_bitcoins = float(input("Introduce la cantidad de bitcoins que tienes"))

codigo_moneda_usuario = ""
mensaje = ""

if tipo_moneda.upper() == "DOLARES":
    codigo_moneda_usuario = "USD"
elif tipo_moneda.upper() == "EUROS":
    codigo_moneda_usuario = "EUR"
elif tipo_moneda.upper() == "LIBRAS":
    codigo_moneda_usuario = "GBP"
else:
    print("No has introducido una moneda correcta")

if codigo_moneda_usuario != "":
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    f = request.urlopen(url)
    datos_json = f.read().decode("utf-8")
    datos_diccionario = loads(datos_json)
    equivalencia = datos_diccionario['bpi'][codigo_moneda_usuario]['rate_float']
    cantidad = cantidad_bitcoins * equivalencia
    mensaje = f"{cantidad_bitcoins} bitcoins equivalen a {cantidad} {tipo_moneda}"
    print(mensaje)


