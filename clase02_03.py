# ej 1

x = 10
if x > 50:
    print("mas grande que 50")
else:
    print("mas pequeno que 50")

''' Comectarios de la linea 9 hasta la linea 16
class Emptyclass:
    pass


for val in my_string:
    pass
'''

# Tipos de datos Primitivos
# valores Booleanos.
is_hungry = True
has_freckles = False

# Numeros
age = 35  # almacena un int
weight = 160.57  # almacena un float

# Texto
name = "carlos Carrasco"

# tipos compuestos.
# Tuplas, un tipo de datos que es inmutable (no se puede modificar después de su creación) y puede contener un grupo de valores. Las tuplas pueden contener tipos de datos mixtos.
print(" ")
print("ej- Tuplas")
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		    # salida: Bruce
# ERROR: no se puede modificar (el objeto 'tupla' no admite la asignación de elementos)
# dog[1] = 'dachshund'

# Listas, un tipo de datos que es mutable y puede contener un grupo de valores. Generalmente destinado a almacenar una colección de datos relacionados.
print(" ")
print("ej- Listas")

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# salida: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')    # Agrega elemento al final de la lista
print(ninjas)               # salida: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()                # Elimina ultimo elemento
print(ninjas)               # salida: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)               # Elimina elemento 'KB'
print(ninjas)               # salida: ['Francis', 'Oliver']

# Diccionario, un grupo de pares clave-valor. Los elementos del diccionario se indexan mediante claves únicas que se utilizan para acceder a los valores. Cuando esté listo, puede encontrar más métodos de diccionario integrados aquí
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	                    # actualiza si la llave existe
# agrega un par clave-valor si la clave no existe
new_person['hobbies'] = ['climbing', 'coding']
# salida: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
print(new_person)
# remueve la clave especifica y retorna el valor
w = new_person.pop('weight')
print(w)		                                # salida: 160.2
# salida: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
print(new_person)

print(type(2.63))		    # salida: <class 'float'>
print(type(new_person))		# salida: <class 'dict'>

print(len(new_person))		# salida: 4 (the number of key-value pairs)
print(len('Coding Dojo'))   # salida: 11

# print("Hello" + 42)		# salida: TypeError
print("Hello " + str(42))   # salida: Hello 42

total = 35
user_val = "26"
# total = total + user_val		# salida: TypeError
total = total + int(user_val)  # total será 61

print(" ")
print("Ej IF")
# porque x no es mayor que 50, la segunda instrucción de impresión es la única que se ejecutará

x = 12
if x > 50:
    print("mayor que 50")
else:
    print("menor que 50")

# aunque x sea mayor que 10 y 50, la primera declaración verdadera es la única que se ejecutará, por lo que solo veremos 'mayor que 10'
x = 55
if x > 10:
    print("mayor que 10")
elif x > 50:
    print("mayor que 50")
else:
    print("menor que 10")

# no sucede nada, porque la declaración es falsa
if x < 10:
    print("menor que 10")

# Bucles For
print(" ")
print("Ej For")

for x in range(0, 10, 1):
    print(x)
print(" ")
for x in range(0, 10):  # incremento de +1 está implícito
    print(x)
print(" ")
for x in range(10):	    # incremento de +1 e inicia en 0 está inplicito
    print(x)
print(" ")

# salida: 0, 2, 4, 6, 8
for x in range(0, 10, 2):
    print(x)

# salida: 5, 2
for x in range(5, 1, -3):
    print(x)


print(" ")
print("ej- bucle for listas")

# salida: 0 abc, 1 123, 2 xyz
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])

print(" ")

# salida: abc, 123, xyz
for v in my_list:
    print(v)

print(" ")
print("ej- bucle for Diccionario")
# salida: name, language
my_dict = {"name": "Noelle", "language": "Python"}
for k in my_dict:
    print(k)

print(" ")

# salida: Noelle, Python
my_dict = {"name": "Noelle", "language": "Python"}
for k in my_dict:
    print(my_dict[k])

print(" ")

'''
# otra forma de iterar a través de claves o llaves
for key in capitals.keys():
    print(key)
# iterar con valores
for val in capitals.values():
    print(val)
# iterar con ambos, llaves y valores
for key, val in capitals.items():
    print(key, " = ", val)
'''

print(" ")
print("Ej while ")

for count in range(0, 5):
    print("looping - ", count)

print(" ")
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

print(" ")
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final de sentencia else")

print(" ")
# salida: s, t, r
for val in "string":
    if val == "i":
        break
    print(val)


print(" ")
# salida: s, t, r, n, g
# Nota, no i en el output, pero el bucle continuo después de la i
for val in "string":
    if val == "i":
        continue
    print(val)


print(" ")
# salida: 3, 2, 1
y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
# solo se ejecuta en una salida limpia del ciclo while (es decir, no un break)
else:
    print("Final else statement")
