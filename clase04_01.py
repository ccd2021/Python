print(" ")
print("Operador ternario")

# syntaxis: <result_if_true> if <condition> else <result_if_false>

# tradicional
stacks = 1
if stacks >= 3:
    print('1.- Coding Dojo')
else:
    print('You are not Coding Dojo!')
# ternario
print('2.- Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')

print(" ")
print("Funciones Lambda ")

'''
class Underscore:
    def map(self, iterable, callback):
        # tu código aqui

    def find(self, iterable, callback):
        # tu código aqui

    def filter(self, iterable, callback):
        # tu código aqui

    def reject(self, iterable, callback):
        # tu código

        # has creado una libreria con 4 métodos
        # se crea la instancia de la clse
_ = Underscore()  # sí, estamos configurando una instancia a una variable que es un guión bajo
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# debe retornar [2, 4, 6] después que termines de implementar el código de arriba
'''

print(" ")
print("Secuencias ")

my_list = [99, 4, 2, 5, -3]
my_tuple = (99, 4, 2, 5, -3)
my_str = "sequoia"
print(my_list[:])                   # salida: [99,4,2,5,-3]
print(my_tuple[1:])                 # salida: (4,2,5,-3)
print(my_str[:3])                   # salida: "seq"
print(my_tuple[2:4])                # salida: (2,5)
# salida: [99,4,2,5,-3] (99,4,2,5,-3) 'sequoia' -- note fíjate que el valor original no cambió
print(my_list, my_tuple, my_str)

print("max", max(my_list))  # devuelve el valor más grande en la secuencia
# devuelve la suma de todos los valores en secuencia
print("sum", sum(my_list))
# sequence aplica la función a cada elemento en la secuencia que pasa. Devuelve una lista de los resultados.
#print("map", map(function))
print("min", min(my_list))  # devuelve el valor más bajo en una secuencia.
# devuelve una lista ordenada de los valores de la secuencia
print("sort", sorted(my_list))
