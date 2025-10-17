class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def imprimirNombre(self):
        print(self.name)

    def imprimirPrecio(self):
        print(self.price)

    def __del__(self):
        print("objeto borrado")

producto1 = Product("Carne", "2kg", "3000")
producto2 = Product("Pollo", "1kg", "2000")