# 1. TAREA: imprimir "Hola mundo"
print("Hola mundo")

# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Carlos Carrasco"
print("Hola", name)  # con una coma
print("Hola " + name)  # con un +

# 3. imprimir "Hola 42!" con un numero en una variable
edad = 52
print("Hola", str(edad)+"!")  # con una coma

caracter = "!"
edad = 52
# con un + - !Este debería darnos un error!
print("Hola  %d %s" % (edad, caracter))

# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "Ensalada Cesar"
fave_food2 = "Salmon"
print("Me encanta comer {} and {}".format(
    fave_food1, fave_food2))  # con .format()
print(f"Me encanta comer {fave_food1} and {fave_food2}")  # con una cadena f


# 5.  practicas de otros metodos....
# Convierte a mayuscula el string
print("")
print("5. practicas de otros metodos, repasados en web......")


string = 'hola carlos'
print('Muestra en mayuscula', string.upper())

# Convierte a minuscula el string
string = 'HOLA CARLOS'
print('Muestra en minuscula', string.lower())

# Numero de ocurrencia de 'P'
message = 'python es popular programming languaje'
print('Numero de ocurrencias de p:', message.count('pop'))

# Busca un string en una cadena y los separa.
text = 'Python is a fun programming language'
print(text.split(' '))

text = 'Python is a fun programming language'
print(text.split('is'))

# Busca un string y entrega la posicion dentro de otro string, sino encuentra nada devuelve -1
text = 'Python is a fun programming language'
print(text.find('fun'))

# testea si variable es alfanumerico
text = 'Alfanumerico99'  # True
print('Variable es ', text.isalnum())

text = 'Carlos Carrasco'  # False
print('Variable es ', text.isalnum())

text = 'Carlos100Carrasco'  # True
print('Variable es ', text.isalnum())

text = '100'  # True
print('Variable es ', text.isalnum())


# testea si variable es alfanumerico
text = 'carlos'
print('Variable con alfanumerico', text.isalpha())

text = 'carlos carrasco'
print('Variable con alfanumerico', text.isalpha())

text = 'carlos100'
print('Variable con alfanumerico', text.isalpha())

# testea si variable es numerico
text = '100'
print('Variable viene con digitos', text.isdigit())

text = '100abc'
print('Variable viene con digitos', text.isdigit())

# detecta si el string viene con minusculas
text = 'abc'
print('Variable viene con minuscula', text.islower())

text = 'ABC'
print('Variable viene con minuscula', text.islower())

# detecta si el string viene con mayusculas
text = 'abc'
print('Variable viene con mayusculas', text.isupper())

text = 'ABC'
print('Variable viene con mayusculas', text.isupper())

# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))


# check if the message ends with fun
message = 'Python is fun'
print(message.endswith('fun'))
print(message.endswith('funy'))
