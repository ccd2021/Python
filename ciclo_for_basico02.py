print("ej01 -Tamano grande")


def biggie_size(lista):

    for x in range(0, len(lista)):
        if lista[x] > 0:
            lista[x] = 'big'

    return lista


resultado = biggie_size([- 1, 3, 5, -5])
print("El resultado de la lista final es:", resultado)


print("")
print("ej02 -Contar positivos")


def count_positives(lista):

    contador_positivos = 0
    for x in range(0, len(lista)):
        if lista[x] > 0:
            contador_positivos += 1

    # print(lista[:])
    # print(len(lista)-1)

    if contador_positivos > 0:
        lista[len(lista)-1] = contador_positivos

    return lista


resultado = count_positives([- 1, 1, 1, 1])
print("El resultado de la lista final es:", resultado)

resultado = count_positives([1, 6, -4, -2, -7, -2])
print("El resultado de la lista final es:", resultado)


print("")
print("ej03 - Suma total")


def sum_total(lista):
    suma = 0
    for x in range(0, len(lista)):
        suma = suma + lista[x]
    return suma


print("la suma es: ", sum_total([1, 2, 3, 4]))
print("la suma es: ", sum_total([6, 3, -2]))


print("")
print("ej04 - Promedio ")


def promedio(lista):
    suma = 0
    for x in range(0, len(lista)):
        suma = suma + lista[x]
    return suma/len(lista)


print("El promedio es:", promedio([1, 2, 3, 4]))


print("")
print("ej05 -  Longitud ")


def longitud(lista):
    return len(lista)


print("Promedio es ", longitud([37, 2, 1, -9]))
print("Promedio es ", longitud([]))


print("")
print("ej06 - Minimo ")


def minimo(lista):

    if len(lista) > 0:
        minimo = lista[0]
        for x in range(0, len(lista)):
            if lista[x] < minimo:
                minimo = lista[x]
        return minimo
    else:
        return False


print("El valor minimo es.",  minimo([37, 2, 1, -9]))
print("El valor minimo es.",  minimo([]))


print("")
print("ej07 - Maximo ")


def maximo(lista):

    if len(lista) > 0:
        maximo = lista[0]
        for x in range(0, len(lista)):
            if lista[x] > maximo:
                maximo = lista[x]
        return maximo
    else:
        return False


print("El valor maximo es.",  maximo([37, 2, 1, -9]))
print("El valor maximo es.",  maximo([]))


print("")
print("ej08 - Analisis final ")


def ultimate_analysis(lista):
    suma = sum_total(lista)
    prom = promedio(lista)
    mini = minimo(lista)
    maxi = maximo(lista)
    larg = longitud(lista)

    #print(suma, promedio)
    dicc = {'SumaTotal': suma, 'Promedio': prom,
            'Minimo': mini, 'Maximo': maxi, 'longitud': larg}
    print(dicc)


ultimate_analysis([37, 2, 1, -9])


print("")
print("ej09 - Lista inversa")


def reverse_list(lista):
    lista.sort()
    print(lista)


reverse_list([37, 2, 1, -9])
