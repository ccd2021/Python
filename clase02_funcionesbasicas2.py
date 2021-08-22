print("ej1-cta_regresiva")


def cta_regresiva(num):
    lista = []
    for x in range(num, 0, -1):
        lista.append(x)

    for x in range(0, len(lista)):
        print("Lista: {}".format(lista[x]))


cta_regresiva(10)


print(" ")
print("ej2- print_and_return")


def print_and_return(lista):
    num1 = lista[0]
    num2 = lista[1]
    print("elemento1: {}".format(num1))
    return num2


a = print_and_return([100, 200])
print("retorno es: ", a)


print(" ")
print("ej3- First Plus Length")


def first_plus_length(lista):
    suma = lista[0]+len(lista)
    print("El primer elemento de la lista es: {}, y la suma del primer elemento mas longitud de la lista es: {}".format(
        lista[0], suma))


first_plus_length([1, 2, 3, 4, 5])
first_plus_length([100, 200, 300, 400, 500])


print(" ")
print("ej4- Valores mayores que el segundo")


def values_greater_than_second(lista):
    lista_new = []

    if len(lista) > 2:
        valor = lista[1]
        for x in range(0, len(lista)):
            if lista[x] > valor:
                lista_new.append(lista[x])
        print("la cantidad de elementos mayor que el segundo elemento son {}, que son:{}".format(
            len(lista_new), lista_new[:]))

    if len(lista_new) < 2:
        return False
    else:
        return True


print("")
print("ej4- caso 1")
valor = values_greater_than_second([5, 2, 3, 2, 1, 4])
print(valor)

print("")
print("ej4- caso 2")
valor = values_greater_than_second([3])
print(valor)


print(" ")
print("ej5- Esta longitud, ese valor")


def length_and_value(tamano, valor):
    lista = []
    for x in range(0, tamano):
        lista.append(valor)
    print("la lista es:", lista[:])


length_and_value(4, 7)
length_and_value(6, 2)
