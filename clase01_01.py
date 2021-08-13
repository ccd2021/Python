nombre = "Carlos Carrasco"
print("Mi nombre es", nombre)
print("Mi nombre es" + " " + nombre)

edad = 52
print("Mi edad es", edad)
print("Mi edad es " + str(edad))

first_name = "Carlos"
last_name = "Carrasco"
age = 52
print(f"mi nombre es {first_name} {last_name} y tengo {age} annos")

first_name = "Carlos"
last_name = "Carrasco"
age = 27
print("Mi nombre es {} {} y tengo {} annos.".format(first_name, last_name, age))
# esta mal puesto el orden de los campos a mostrar
print("Mi nombre es {} {} y tengo {} annos.".format(age, first_name, last_name))

hw = "Hola %s" % "mundo" 	# con valores literales
py = "Me encanta Python %d" % 3
print(hw, py)

name = "Carlos C"
age = 52
print("Mi nombre es %s y soy %d" % (nombre, edad))

x = "hola mundo"
print(x.title())

print('')
print('Ejercicio 2')

# Convierte a mayuscula el string
string = 'hola carlos'
print(string.upper())

# Convierte a minuscula el string
string = 'HOLA CARLOS'
print(string.lower())

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
