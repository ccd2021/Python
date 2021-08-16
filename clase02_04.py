print("Ej1- Funciones")


def add(a, b):      # nombre de la función: 'add', parámetros: a y b
    x = a + b       # proceso
    return x        # retorno value: x


new_val = add(3, 5)  # llamando a la función add, con los argumentos 3 y 5
# el resultado de la función add se devuelve y se guarda en new_val, por lo que veremos 8
print("resultado de la funcion add es:", new_val)


print("")
print("Ej2- Funciones")


def say_hi(name):
    # print("Hola, " + name)
    return "Hola " + name


# invocando la función 3 veces, pasando un argumento cada vez;
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

# el valor devuelto por la función se asigna a la variable
greeting = say_hi("Carlos Carrasco")
print(greeting)                         # mostrará 'Hi Michael'

# ejemplos con add
sum1 = add(4, 6)
sum2 = add(1, 4)
sum3 = sum1 + sum2
print("")
print("La suma de sum1 +sum2 es:", sum3)

# Asignatura: Funciones Básicas I

print(" ")
print("# Asignatura: Funciones Básicas I")
print("#1")

# 1


def a():
    return 5


print(a())

print(" ")
print("#2")

# 2


def a():
    return 5


print(a()+a())

print(" ")
print("#3")
# 3


def a():
    return 5
    return 10


print(a())

print(" ")
print("#4")
# 4


def a():
    return 5
    print(10)


print(a())

print(" ")
print("#5")
# 5


def a():
    print(5)


x = a()
print(x)


print(" ")
print("#6")
# 6

'''
def a(b, c):
    print(b+c)


print(a(1, 2) + a(2, 3))
'''

print(" ")
print("#7")
# 7


def a(b, c):
    return str(b)+str(c)


print(a(2, 5))

print(" ")
print("#8")
# 8


def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7


print(a())

print(" ")
print("#9")
# 9


def a(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(a(2, 3))
print(a(5, 3))
print(a(2, 3) + a(5, 3))


print(" ")
print("#10")
# 10


def a(b, c):
    return b+c
    return 10


print(a(3, 5))


print(" ")
print("#11")
# 11
b = 500
print(b)


def a():
    b = 300
    print(b)


print(b)
a()
print(b)


print(" ")
print("#12")
# 12
b = 500
print(b)


def a():
    b = 300
    print(b)
    return b


print(b)
a()
print(b)


print(" ")
print("#13")
# 13
b = 500
print(b)


def a():
    b = 300
    print(b)
    return b


print(b)
b = a()
print(b)


print(" ")
print("#14")
# 14


def a():
    print(1)
    b()
    print(2)


def b():
    print(3)


a()


print(" ")
print("#15")
# 15


def a():
    print(1)
    x = b()
    print(x)
    return 10


def b():
    print(3)
    return 5


y = a()
print(y)
