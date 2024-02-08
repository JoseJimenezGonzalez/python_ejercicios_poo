class Cerveza:
    _codigo_incremental = 0

    def __init__(self, nombre, tipo, elaboracion_artesanal, precio, existencias):
        self._codigo = "CERV-" + str(Cerveza._codigo_incremental)
        Cerveza._codigo_incremental += 1
        self._nombre = nombre
        self._tipo = tipo
        self._elaboracion_artesanal = elaboracion_artesanal
        self._precio = precio
        self._existencias = existencias

    def servir_cerveza(self, cantidad):
        if cantidad <= self._existencias:
            self._existencias -= cantidad
            print(f"Se han servido {cantidad} unidades de {self._nombre}.")
        else:
            print(f"No hay suficientes existencias de {self._nombre} para servir {cantidad} unidades.")
            self._existencias = 0

    def reponer_cerveza(self, cantidad):
        self._existencias += cantidad
        print(f"Se han repuesto {cantidad} unidades de {self._nombre}.")

    def __eq__(self, other):
        return self._codigo == other._codigo

    def __str__(self):
        return f"Código: {self._codigo}, Nombre: {self._nombre}, Tipo: {self._tipo}, Elaboración Artesanal: {self._elaboracion_artesanal}, Precio: {self._precio}, Existencias: {self._existencias}"


# Ejemplo de uso
cerveza1 = Cerveza("Mahou", "Rubia", False, 2.5, 100)
cerveza2 = Cerveza("Estrella Galicia", "Rubia", True, 3.0, 50)

print(cerveza1)
print(cerveza2)

cerveza1.servir_cerveza(80)
cerveza2.servir_cerveza(60)

cerveza1.reponer_cerveza(30)

print(cerveza1 == cerveza2)
