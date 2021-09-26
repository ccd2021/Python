class perro:

    def __init__(self, nombre, edad, raza, tamanio="Pequeno"):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.tamanio = tamanio

    def sentarse(self):
        print("Estoy sentado")

    def __str__(self):
        return ("Me llamo {}, tengo {} annios y soy de tamanio {}".format(self.nombre, self.edad, self.tamanio))


mascota = perro("Chocolate", 3, "cocker")
mascota.sentarse()
mascota.nombre = "OtroNombre"
print(mascota.nombre)
print(mascota.tamanio)
print(mascota)


class Vehiculo():
    __annioFabricacion = ''

    def __init__(self, num_ruebas):
        self.num_ruebas = num_ruebas

    def setAnnioFabricacion(annio):
        self.__annioFabricacion = annio

    def getAnnioFabricacion(self):
        return self.__annioFabricacion


class Moto(Vehiculo):
    def __init__(self, num_ruedas):
        super().__init__(num_ruebas)


class Trailer(Vehiculo):
    __tonelaje = 0

    def __init__(self, num_ruedas, toneladas):
        super().__init__(num_ruebas)
        self.__tonelaje = toneladas

    def getTonelaje(self):
        return self.__tonelaje

    def setTonelaje(self):
        pass
