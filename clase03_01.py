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
