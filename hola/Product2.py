class Product:
    def __init__(self, name, quantity, price):
        self.__name = name
        self.quantity = quantity
        self.price = price
    
    def imprimirNombre(self):
        print(self.__name)

    def setPrice(self, price):
        self.price = price

producto = Product("Hola", "123", "1232")
producto.imprimirNombre()

producto.setPrice("400")
print(producto.price)