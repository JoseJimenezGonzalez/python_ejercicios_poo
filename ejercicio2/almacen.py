#a) Crear la clase Producto que tiene los atributos nombre, identificador (código
#alfanumérico) y precio. Tiene que tener constructor, __str__ y __eq__, donde
#un producto es igual a otro cuando tienen el mismo identificador. También
#tendrá el método comprar que tiene como parámetro las unidades a llevarse. El
#método comprar devuelve un float con el precio multiplicado por la unidades
#que se quiere llevar. Si al comprar se lleva más de 50 unidades el precio final
#se reduce a la mitad.

class Producto:
    def __init__(self, nombre, identificador, precio):
        self._nombre = nombre
        self._identificador = identificador
        self._precio = precio
    def __str__(self):
        return f"Nombre: {self._nombre}, identificador: {self._identificador} y precio: {self._precio}"
    def __eq__(self, other):
        return self._identificador == other._identificador
    def comprar(self, unidades):
        if(unidades > 50):
            precio = unidades * self._precio / 2
        else:
            precio = unidades * self._precio
        return precio

#b) Crear la clase Perecedero que hereda de Producto. Se añade un atributo
#más que es los días para caducar. Hay que hacer el método __str__. El método
#comprar es similar al de producto solo que le reduce el precio calculado en la
#clase Producto según los días que le queden para caducar:
#a) Si le queda un día para caducar, el precio final es la cuarta parte del
#que devuelve comprar de la clase Producto.
#b) Si le quedan 2 días para caducar, el precio final es la tercera parte.
#c) Si le quedan 3 días para caducar, el precio final es la mitad.
#d) Si le quedan 4 o más días no se modifica el precio original.
class Perecedero(Producto):
    def __init__(self, nombre, identificador, precio, dias_caducar):
        super().__init__(nombre, identificador, precio)
        self._dias_caducar = dias_caducar
    def __str__(self):
        return f"Nombre: {self._nombre}, identificador: {self._identificador}, precio: {self._precio} y dias para caducar: {self._dias_caducar}"
    def comprar(self, unidades):
        if(self._dias_caducar == 1):
            precio = super().comprar(unidades)/4
        elif(self._dias_caducar == 2):
            precio = super().comprar(unidades) / 3
        elif(self._dias_caducar == 3):
            precio = super().comprar(unidades) / 2
        else:
            precio = super().comprar(unidades)
        return precio
#c) Crear la clase Tienda como se describe a continuación:
#o La clase tiene 1 atributo que es una lista que está inicialmente vacía.
#o La clase tendrá un método para añadir objetos de las clases anteriores
#llamado nuevo_producto a la lista anteriormente mencionada. El método
#recibe objetos de la clase Producto y Perecedero.
#o La clase Tienda también tendrá un método __str__ uniendo todos los
#datos de todos los productos que haya en la lista (Producto o
#Perecedero), llamando al método __str__ correspondiente.
class Tienda:
    def __init__(self):
        self._lista_productos = []

    def nuevo_producto(self, producto):
        self._lista_productos.append(producto)

    def __str__(self):
        res = ""
        for producto in self._lista_productos:
            res += producto.__str__() + "\n"
        return res

tienda = Tienda()
producto1 = Producto("Camisa", "A001", 20)
perecedero1 = Perecedero("Leche", "P001", 2, 3)
tienda.nuevo_producto(producto1)
tienda.nuevo_producto(perecedero1)
print(tienda)