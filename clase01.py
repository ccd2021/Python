#print("Hola desde archivo")

nombre = "carlos"
apellido = "carrasco"

print("Hola " + nombre + " " + apellido)

print("Hola {} {}".format(nombre, apellido))


def saludo(nombre):
    return("Hola {}".format(nombre))


# Invocando una funcion saludo
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
print("")
print("Arreglos")

colores = ['rojo', 'verde', 'azul', 12]
print(" ")
print("ej 1")
for color in colores:
    print(color)

print(" ")
print("ej 2")
for i in colores:
    print(i)


# Diccionarios
print("")
print("Diccionarios")

menu = {'lunes': 'pasta', 'martes': 'pizza',
        'miercoles': 'pescado', 'jueves': ['vegetales', 'papa']}

# aca solo muestra los indices del diccionario.
print(" ")
print("ej 1")
print(menu.keys())

# aca solo muestra el valor del indice lunes, en este caso pasta
print(" ")
print("ej 2")
print(menu['lunes'])

# aca muestra los valores del diccionario
print(" ")
print("ej 3")
for k in menu.values():
    print(k)

# aca muestra el valor de un arreglo q esta en el jueves.
print(" ")
print("ej 4")
print(menu['jueves'][0])
print(menu['jueves'][1])

#n,m = 5,6

n = 5
m = 6


def imprime_matriz(num_filas, num_cols):
    for i in range(0, num_filas - 1):
        print("*" * num_cols)


print(" ")
print("ejercicio 5")
imprime_matriz(n, m)


def numeros_primos(inicio, fin):
    contador = inicio
    num_primos = 0
    # contar desde n a m
    while (contador <= fin):  # desde inicio a fin
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


print(" ")
print("ejercicio 6")
numeros_primos(1, 20)
