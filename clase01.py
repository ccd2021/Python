#print("Hola desde archivo")

nombre = "carlos"
apellido = "carrasco"

print("Hola " + nombre + " " + apellido)

print("Hola {} {}".format(nombre, apellido))


def saludo(nombre):
    return("Hola {}".format(nombre))


print(saludo("carlos Alberto ..."))


def mayor_de_edad(edad, nombre):
    if (edad >= 18):
        print("{}, Eres mayor de edad".format(nombre))
    else:
        annios_faltantes = 18 - edad
        print("{}, Te faltan : {} años para ser mayor de edad ".format(
            nombre, annios_faltantes))


nombre = "carlos"
edad = 12
mayor_de_edad(edad, nombre)
saludo(nombre)


def suma_producto(a, b):
    suma = a + b
    producto = a * b
    return suma, producto


print(suma_producto(10, 5))


# Arreglos
colores = ['1', '2', '3']

for color in colores:
    print(color)


# Diccionarios

menu = {'lunes': 'pasta', 'martes': 'pizza',
        'miercoles': 'pescado', 'jueves': ['vegetales', 'papa']}
print(menu.keys())
print('')

print(menu['lunes'])
print('')


for k in menu.values():
    print(k)


print(menu['jueves'][0])
print(menu['jueves'][1])
