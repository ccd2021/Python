# Clase2 :: programacion orientada a objetos ::

Perro = {
    "nombre": "Avellana",
    "Edad": 4,
    "raza": "cocker",
    "tamano": "Grande"
}

Perro2 = {
    "nombre": "Choco",
    "Edad": 4,
    "raza": "cocker",
    "tamano": "Grande"
}


class Perro:

    def __init__(self, nombre, edad, raza, tamanio="Pequeño"):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.tamanio = tamanio

    def sentarse(self):
        print("Estoy sentado")

    def __str__(self):
        return("me llamo {}, tengo {} annios y soy de tamanio {}".format(self.nombre, self.edad, self.tamanio))


print("")
print("Ej 1")

mascota = Perro("chocolate", 3, "cocker")
mascota.sentarse()
mascota.nombre = "otroNombre"

print("")
print("Ej 2")

print(mascota.nombre)
print(mascota.tamanio)
print(mascota)


# Herencia
print("")
print("Herencia ej 1")


class Vehiculo():
    __annioFabricacion = ''

    def __init__(self, num_ruedas):
        self.num_ruedas = num_ruedas

    def setAnnioFabricacion(self, annio):
        self.__annioFabricacion = annio

    def getAnnioFabricacion(self):
        return self.__annioFabricacion

    def __str__(self):
        return("Soy un Vehiculo de {} ruedas".format(self.num_ruedas))


class Moto(Vehiculo):
    def __init__(self, num_ruedas):
        super().__init__(num_ruedas)


class Trailer(Vehiculo):
    __tonelaje = 0

    def __init__(self, num_ruedas, toneladas):
        super().__init__(num_ruedas)
        self.__tonelaje = toneladas

    def getTonelage(self):
        return self.__tonelaje

    def setTonelaje(self, toneladas):
        self.__tonelaje = toneladas


moto = Moto(2)
trailer = Trailer(8, 1000)

print(moto)
print(trailer)

trailer.setAnnioFabricacion('2010')
print(trailer.getAnnioFabricacion())
