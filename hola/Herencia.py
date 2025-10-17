class Transport:
    def __init__(self, name):
        self.name = name

    def imprimirNomber(self):
        print(self.name)

class Terrestre(Transport):
    def __init__(self, name, ruedas):
        super().__init__(name)
        self.ruedas = ruedas

    def imprimirRuedas(self):
        print(self.ruedas)

class Maritimo(Transport):
    def __init__(self, name, motores):
        super().__init__(name)
        self.motores = motores

carro = Terrestre("Toyota", "4 ruedas")
barco = Maritimo("Barco", "4 motores")

carro.imprimirNomber()
barco.imprimirNomber()

carro.imprimirRuedas()