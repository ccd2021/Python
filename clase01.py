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
    elif (edad == 10):
        return("edad es 10")
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


print("ejercicio 1")

#n,m = 5,6

n = 5
m = 6


def imprime_matriz(num_filas, num_cols):
    for i in range(0, num_filas - 1):
        print("*" * num_cols)


imprime_matriz(n, m)

print("ejercicio 2")


def numeros_primos(inicio, fin):
    contador = inicio
    num_primos = 0
    # contar desde n a m
    while (contador <= fin):
        divisibles = 0
        i = 1
        while (i <= contador):
            if (contador % i == 0):
                divisibles += 1
            i += 1
        if divisibles == 2:
            num_primos += 1
        contador += 1
    print("Entre {} y {} hay {} numeros primos".format(inicio, fin, num_primos))


numeros_primos(1, 20)

print("")
print("ejercicio 3")
