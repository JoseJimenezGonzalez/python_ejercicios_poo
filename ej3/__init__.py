class Joya:
    _codigo_incremental = 0

    def __init__(self, nombre, marca, tipo, precio, peso_gramos, quilates):
        self._codigo = "JOYA-" + str(Joya._codigo_incremental)
        Joya._codigo_incremental += 1
        self._nombre = nombre
        self._marca = marca
        self._tipo = tipo
        self._precio = precio
        self._peso_gramos = peso_gramos
        self._quilates = quilates

    def pureza(self):
        pureza = (self._quilates * 4.167) / self._peso_gramos
        return pureza

    def __eq__(self, other):
        return self._codigo == other._codigo

    def __str__(self):
        return f"Código: {self._codigo}, Nombre: {self._nombre}, Marca: {self._marca}, Tipo: {self._tipo}, Precio: {self._precio}, Peso (gramos): {self._peso_gramos}, Quilates: {self._quilates}"


# Ejemplo de uso
joya1 = Joya("Anillo de compromiso", "Tiffany & Co.", "Anillo", 5000, 5, 24)
joya2 = Joya("Collar de perlas", "Cartier", "Collar", 8000, 20, 18)

print(joya1)
print(joya2)

print(f"Pureza del oro en la joya 1: {joya1.pureza()}%")
print(f"Pureza del oro en la joya 2: {joya2.pureza()}%")

print(joya1 == joya2)
