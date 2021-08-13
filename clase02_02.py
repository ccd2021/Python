class Persona():
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def saludar(self):
        print(f"Hola mi es {self.nombre}")
        #print("Hola mi nombre es {}".format(self.nombre))


class Instructor(Persona):
    def __init__(self, nombre, email, curso):
        super().__init__(nombre, email)
        self.curso = curso

    def saludar(self):
        # super().saludar()
        return("Mi nombre es {} y soy instructor de {}".format(self.nombre, self.curso))


class Estudiante(Persona):
    def __init__(self, nombre, email, cohort):
        super().__init__(nombre, email)
        self.cohort = cohort

    def saludar(self):
        super().saludar()
        print("Soy estudiante del cohort de {}".format(self.cohort))


class Bootcamp():
    __ListaEstudiantes = []

    def __init__(self, nombre, zoom_link, instructor):
        self.nombre = nombre
        self.zoom_link = zoom_link
        self.instructor = instructor

    def getInstructorBootcamp(self):
        return self.instructor.saludar()

    def agregarEstudiante(self, estudiante):
        self.__ListaEstudiantes.append(estudiante)

    def getEstudiantes(self):
        for estudiante in self.__ListaEstudiantes:
            estudiante.saludar()


inst = Instructor(nombre="Patricio",
                  email="patricio@gmail.com", curso="Python")
est1 = Estudiante("maria", "maria.gomez@gmail.com", "Agosto2021")
est2 = Estudiante("Ana", "ana@gmail.com", "Agosto2021")

Bootcamp_Agosto = Bootcamp("Python Full Stack", "link", inst)
print("Nombre del Bootcamp:", Bootcamp_Agosto.nombre)
print(Bootcamp_Agosto.getInstructorBootcamp())

Bootcamp_Agosto.agregarEstudiante(est1)
Bootcamp_Agosto.agregarEstudiante(est2)
print("-----------------")
Bootcamp_Agosto.getEstudiantes()
