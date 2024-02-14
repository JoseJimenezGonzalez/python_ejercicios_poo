from urllib import request
from json import loads

tipo_moneda = input("Mete el tipo de  moneda a cambiar: ")
tipo_retorno = input("Mete el tipo de moneda a convertir: ")
cantidad_dinero_convertir = float(input("Cantidad de dinero a convertir: "))
direccion = "https://open.er-api.com/v6/latest/" + tipo_moneda
f = request.urlopen(direccion)
datos = f.read().decode("utf-8")
objeto_datos = loads(datos)
objeto_rates = objeto_datos['rates']
cambio = objeto_rates[tipo_retorno]
conversion = cantidad_dinero_convertir * cambio
print(conversion)