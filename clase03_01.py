import random


def beCheerful(name='', repeat=2):		# asignar defaults cuando se declare los parámetros
    print(f"Buenos dias {name}\n" * repeat)


# salida: good morning (repeated on 2 lines)
beCheerful()
# salida: good morning tim (repeated on 2 lines)
beCheerful("tim")
# salida: good morning john (repeated on 2 lines)
beCheerful(name="john")
# salida: good morning (repeated on 6 lines)
beCheerful('CCD', repeat=6)
# salida: good morning michael (repeated on 5 lines)
beCheerful(name="michael", repeat=5)
# NOTA: el orden de loa argumentos no importa si estamos implícitos al enviar nuestros argumentos!
beCheerful(repeat=3, name="kb")

print(" ")
print("Ej Random ")


def randInt(min=0, max=0):
    if min == 0 and max == 0:
        num = round(random.random() * 100, 2)
        print("Funcion sin argumentos", num)
    elif(min == 0 and max > 0):
        num = round(random.random() * max, 2)
        print("Funcion solo con max", num)
    elif(min > 0 and max == 0):
        num = round(random.random() * min, 2)
        print("Funcion solo con min", num)
    else:
        num = round(random.random(), 0)
        print("Funcion solo con min y max", num)
    return num


randInt()
randInt(max=50)
randInt(min=50)
randInt(min=50, max=500)


print(" ")
print("Ej Listas ")

lista = ['a', 'b', 'd', 'i', 'j']
print("01", lista[0])  # Primer elemento de la lista. Índice 0, 'a'
print("02", lista[3])  # Cuarto elemento de la lista. Índice 3, 'i'

lista = ['a', ['d', 'b'], 'z']
print("03", lista[1][1])  # lista[1] hace referencia a la lista anidada,'b'

vocales = ['a', 'e', 'i', 'o', 'u']
print("04", vocales[-1])    # resultado es 'u'

print("05", vocales[-4])    # resultado es 'e'


vocales = ['a', 'e', 'i', 'o', 'u']
# Elementos desde el índice 2 hasta el índice 3-1,    ['i']
print("06", vocales[2:3])
# Elementos desde el 2 hasta el índice 4-1,           ['i', 'o']
print("07", vocales[2:4])
# Todos los elementos,                                ['a', 'e', 'i', 'o', 'u']
print("08", vocales[:])
# Elementos desde el índice 1,                        ['e', 'i', 'o', 'u']
print("09", vocales[1:])
# Elementos hasta el índice 3-1,                      ['a', 'e', 'i']
print("10", vocales[:3])


print(" ")
print("recorriendo un lista de colores")
colores = ['azul', 'blanco', 'negro']
for color in colores:
    print(color)

vocales = ['a']
vocales.append('e')  # Añade un elemento
print("Se muestra lista entera....", vocales)

vocales.extend(['i', 'o', 'u'])  # Añade un grupo de elementos
print("Se muestra lista entera....", vocales)

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
nueva_lista = lista_1 + lista_2
print("Lista es:", nueva_lista)      # [1, 2, 3, 4, 5, 6]

print(" ")
numeros = [1, 2, 3]
numeros *= 3
print("Repite lista N veces *=3 ", numeros)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]


print(" ")
vocales = ['a', 'e', 'u']
vocales.insert(2, 'i')
print("Inserta desde la posicion 2", vocales)     # ['a', 'e', 'i', 'u']


print(" ")
vocales = ['o', 'o', 'o', 'o', 'u']
# Actualiza el elemento del índice 0
vocales[0] = 'a'
print(vocales)                                  # ['a', 'o', 'o', 'o', 'u']
# Actualiza los elementos entre las posiciones 1 y 2
vocales[1:3] = ['e', 'i']
print(vocales)                                  # ['a', 'e', 'i', 'o', 'u']


print(" ")
print("Diccionarios 01")

# salida: Noelle, Python
my_dict = {"name": "Noelle", "language": "Python"}
for k in my_dict:
    print(my_dict[k])


print(" ")
print("Diccionarios 02")

my_dict = {"John": 1, "Michael": 2, "Shawn": 3}

list_of_key = list(my_dict.keys())
list_of_value = list(my_dict.values())

position = list_of_value.index(1)
print(list_of_key[position])

position = list_of_value.index(2)
print(list_of_key[position])

position = list_of_value.index(3)
print(list_of_key[position])


print(" ")
print("Diccionarios 03")

lstdict = [
    {"name": "Klaus", "age": 32},
    {"name": "Elijah", "age": 33},
    {"name": "Kol", "age": 28},
    {"name": "Stefan", "age": 8}
]


# print(next(x for x in lstdict if x["name"] == "Klaus"))
# print(next(x for x in lstdict if x["name"] == "Stefan"))
# print(next((x for x in lstdict if x["name"] == "David"), 'No existe'))
# print(next((i for i, x in enumerate(lstdict) if x["name"] == "Kol"), None))
# print([x for x in lstdict if x['name'] == 'Klaus'][0])

for x in lstdict:
    print(x['name'], x['age'])


print(" ")
lista = [{'Nombre': 'NUCLEO', 'Id': 20, 'Tipo': 'MP', 'Fuente': 2},
         {'Nombre': 'PVC de mexichem', 'Id': 19, 'Tipo': 'MP', 'Fuente': 2}]

# accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
for elem in lista:
    v_linea = ''
    for k, v in elem.items():  # acedemos a cada llave(k), valor(v) de cada diccionario
        print(k, v)
        print(elem.items())
        print(elem.keys())
        print(elem.values())
        if type(v) == int:
            v = str(v)
        v_linea = v_linea + k + '-' + v + ', '
    print(v_linea)
