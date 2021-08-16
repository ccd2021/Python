print("Ej1- Imprimir todods los enteros del 0 al 150")
for x in range(0, 151, 1):
    print(x)

print("")
print("Ej2- Imprimir todos los multiplos de 5, del 5 al 1000")
for x in range(5, 1001, 1):
    # print(x)
    if (x % 5) == 0:
        print("Es multiplo de 5 el:", x)

print("")
print("Ej3- Imprimir enteros del 1 al 100, si es divisible por 5, imprimir Coding en su lugar, si es divisible por 10 imprimir Coding Dojo")
for x in range(1, 101, 1):
    print("numero actual es {}".format(x))
    if (x % 5) == 0:
        print("5-Coding")
    if (x % 10) == 0:
        print("10-Coding Dojo")

print("")
print("Ej4- Ufff, Eso es bastante grande, suma enteros impares de 0 a 500,000 e imprime la suma final.")

num_hasta = 500000
suma_pares = 0
suma_impares = 0
for x in range(0, num_hasta, 1):
    # print(x)
    if (x % 2) == 0:
        suma_pares = suma_pares + x
    else:
        suma_impares = suma_impares + x

# print("La sumatoria de numeros pares   de 0 hasta {} es: {}".format(
#    num_hasta, suma_pares))
print("La sumatoria de numeros impares de 0 hasta {} es: {}".format(
    num_hasta, suma_impares))

print("")
print("Ej5- Cuenta regresiva por cuatro : imprime numeros positivos del 2018 al 0, restando 4 en cada iteracion.")
for x in range(2018, 0, -4):
    print(x)


print("")
print("Ej6- Contador flexible...")
lowNum = 2
highNum = 9
mult = 3

highNum = highNum + 1
for x in range(lowNum, highNum):
    if (x % mult) == 0:
        print(x)


print("")
print("Bonus- Numeros primos")


def numeros_primos(inicio, fin):

    listaPrimos = []
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
            listaPrimos.append(contador)
            num_primos += 1
        contador += 1

    print("Entre {} y {} hay {} numeros primos".format(inicio, fin, num_primos))
    for i in range(0, len(listaPrimos)):
        print("{} el numero primo es {}".format(i, listaPrimos[i]))


numeros_primos(1, 20)
