import random


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
