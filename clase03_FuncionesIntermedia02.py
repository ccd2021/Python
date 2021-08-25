x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


print(" ")
print("ej 1.1 -cambiar en lista x, cambiar 10 por 15 ")

for a in range(0, len(x)):
    if x[a][0] == 10:
        x[a][0] = 15

print(x)


print(" ")
print("ej 1.2 -Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'")

for x in range(0, len(students)):
    for clave in students[x].keys():
        print(students[x][clave])
        if students[x][clave] == 'Jordan':
            students[x][clave] = 'Bryant'

print(" ")
for x in range(0, len(students)):
    for clave in students[x].keys():
        print(students[x][clave])

print(" ")
print("ej 1.3 -En el directorio sports_directory, cambia 'Messi' a 'Andres")

# my_dict = {"name": "Noelle", "language": "Python"}
# for k in my_dict:
#     print(my_dict[k])

print(" ")
for k in sports_directory:
    for i in range(0, len(sports_directory[k])):
        print(sports_directory[k][i])

print(" ")
for k in sports_directory:
    for i in range(0, len(sports_directory[k])):
        if sports_directory[k][i] == 'Messi':
            sports_directory[k][i] = 'Andres'
        print(sports_directory[k][i])

print(" ")
print("ej 1.4 -Camba el valor 20 en z a 30")

for x in range(0, len(z)):
    for clave in z[x].keys():
        print(z[x][clave])
print(" ")
for x in range(0, len(z)):
    for clave in z[x].keys():
        if z[x][clave] == 20:
            z[x][clave] = 30
        print(z[x][clave])

print(" ")
print("ej 2.0 -Itera a traves de una lista de diccionarios")


def iterateDictionary(lista):
    # accedemos a cada elemento de la lista (en este caso cada elemento es un diccionario)
    for elem in lista:
        v_linea = ''
        for k, v in elem.items():  # acedemos a cada llave(k), valor(v) de cada diccionario
            if type(v) == int:
                v = str(v)
            v_linea = v_linea + k + ' - ' + v + ', '

        print(v_linea)


students2 = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(students2)


print(" ")
print("ej 3.0 -Obten valores de una lista de diccionarios")


def iterateDictionary2(key_name, lista):
    for elem in lista:
        for k, v in elem.items():
            if k == key_name:
                print(v)


students2 = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary2('first_name', students2)
print(" ")
iterateDictionary2('last_name', students2)

print(" ")
print("ej 4.0 -Itera a traves de un diccionario con valores de listas")


def printInfo(dicc):
    for k in dicc.keys():
        # print(k)
        for v in dicc.values():
            # print(v)
            print(str(len(v)) + '-'+k)
            for i in range(0, len(v)):
                print(v[i])
            print(" ")


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
