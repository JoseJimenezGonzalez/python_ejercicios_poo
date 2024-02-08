class Libro:
    def __init__(self, titulo, isbn, autor, ejemplares_totales):
        self._titulo = titulo
        self._isbn = isbn
        self._autor = autor
        self._ejemplares_totales = ejemplares_totales
        self._ejemplares_prestados = 0

    def __str__(self):
        return f"Título: {self._titulo}, ISBN: {self._isbn}, Autor: {self._autor}, Ejemplares Totales: {self._ejemplares_totales}, Ejemplares Prestados: {self._ejemplares_prestados}"

    def __eq__(self, other):
        return self._isbn == other._isbn

    def prestamo(self):
        if self._ejemplares_prestados < self._ejemplares_totales:
            self._ejemplares_prestados += 1
            print("Préstamo realizado con éxito.")
        else:
            print("No quedan ejemplares disponibles para prestar.")

    def devolucion(self):
        if self._ejemplares_prestados > 0:
            self._ejemplares_prestados -= 1
            print("Devolución realizada con éxito.")
        else:
            print("No hay ejemplares prestados para devolver.")


# Ejemplo de uso
libro1 = Libro("El nombre del viento", "9788401352836", "Patrick Rothfuss", 5)
libro2 = Libro("Cien años de soledad", "9780307350408", "Gabriel García Márquez", 3)

print(libro1)
print(libro2)

libro1.prestamo()
libro1.prestamo()
libro1.devolucion()
libro2.prestamo()
libro2.devolucion()
libro2.devolucion()
