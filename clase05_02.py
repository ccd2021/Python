print("")
print("Tienda y Productos")


class tienda:
    def __init__(self, nombre, lista_prod):
        self.nombre = nombre
        self.lista_prod = lista_prod


class producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria


print("")
print("Argumentos multiples")


def varargs(arg1, *args):
    print("Got ", arg1, " and ", args)


varargs("one") 			        # salida: Got one and ()
varargs("one", "two") 	        # salida: Got one and ('two',)
varargs("one", "two", "three")  # salida: Got one and ('two', 'three')
varargs("one", "two", "three", "444", "555")


def varargs1(arg1, *args):
    for a in args:
        print(a)


varargs1("one", "two", "three")  # salida: two, three (on separate lines)


print("")
print("Asignatura: MathDojo, ej1")


def sumar(*valores):
    res = 0
    for val in valores:
        res += val

    return res


print(sumar())
print(sumar(1))
print(sumar(1, 2, 3, 4))

print("")
print("Asignatura: MathDojo, ej2")


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        # tu código aquí
        self.result += num
        sum = 0
        for val in nums:
            sum += val

        self.result += sum
        return self

    def subtract(self, num, *nums):
        # tu código aquí
        self.result -= num

        sum = 0
        for val in nums:
            sum += val

        self.result -= sum
        return self


# crear una instruccion:
md = MathDojo()
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)

p1 = MathDojo()
#resAdd = p1.add(2500).add(2000, 1000, 500).add(500, 3000, 3000, 3000, 500).result
#resSub = p1.subtract(1).subtract(2).subtract(3).result

res_add = p1.add(2500).add(2000, 1000, 500).add(
    1000, 2000, 3000, 4000, 5000).result                        # 21000
res_sub = p1.subtract(1000).subtract(
    1000, 2000, 2000).subtract(1000, 2000, 2000, 5000).result   # 5000
print(res_add, res_sub)


print("")
print("Listas Vinculadas...")


class SLNode:

    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):  # agrega la linea, toma un valor
        # crea una instancia de la clase Node usando el valor dado
        new_node = SLNode(val)
        # salva la cabecera actual en una variable
        current_head = self.head
        # Coloca el proximo nodo en la lista de la cabecera actual
        new_node.next = current_head
        # Coloca la lista de la cabecera al nodo que se creó en el paso anterior
        self.head = new_node
        # return self para permitir las cadenas
        return self

    def print_values(self):
        runner = self.head          # un puntero al primer nodo de la lista
        while (runner != None):     # iterando mientras el corredor es un nodo y no ninguno
            print(runner.value)     # imprimir el valor del nodo actual
            runner = runner.next 	# Establecer el corredor a su vecino
        # Una vez que el bucle está terminado, regrese a sí mismo para permitir el encadenamiento
        return self

    def add_to_back(self, val):	    # acepta un valor
        if self.head == None:	    # si la lista está vacia
            self.add_to_front(val)  # ejecuta el método add_to_front
            # asegurémonos de que el resto de esta función no suceda si agregamos al frente
            return self

        # crea una nueva instancia de nuestra clase Node con el valor dado
        new_node = SLNode(val)
        # establece un iterador para que comience al principio de la lista
        runner = self.head
        while (runner.next != None):  # iterador hasta que el iterador no tenga un vecino
            # Incrementa el corredor al siguiente nodo de la lista.
            runner = runner.next
        # Incrementa el corredor al siguiente nodo de la lista.
        runner.next = new_node


'''
print("")
print("Recorriendo una lista...")

my_list = SList()  # crear una nueva instancia de una lista

my_list.add_to_front("are").add_to_front(
    "Linked lists").add_to_back("fun!").print_values()
'''

print("")
print("Herencia...")

'''
class CheckingAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        # code
        pass

    def withdraw(self, amount):
        # code
        pass

    def write_check(self, amount):
        # code
        pass

    def display_account_info(self):
        # code
        pass


class RetirementAccount:
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.is_roth = is_roth

    def deposit(self, amount):
        # código - evaluar impuestos si es necesario
        pass

    def withdraw(self, amount):
        # código - evaluar impuestos si es necesario
        pass

    def display_account_info(self):
        # codigo
        pass
'''

'''
class CheckingAccount(BankAccount):
    pass


class RetirementAccount(BankAccount):
    pass
'''


class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def withdraw(self, amount):
        # if (self.balance - amount) > 0:
        #    self.balance -= amount
        # else:
        #    print("INSUFFICIENT FUNDS")
        # return self

        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self


class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth

    def withdraw(self, amount, is_early):
        # if is_early:
        #    amount = amount * 1.10
        # if (self.balance - amount) > 0:
        #    self.balance -= amount
        # else:
        #    print("INSUFFICIENT FUNDS")
        # return self

        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self


print("")
print("Anulacion y polimorfismo...")


print("")
print("Anulacion...")


class Parent:
    def method_a(self):
        print("invocando PARENT method_a!")


class Child(Parent):
    def method_a(self):
        print("invocando CHILD method_a!")


dad = Parent()
son = Child()
dad.method_a()
son.method_a()  # ¡nota que esto anula el método Parent!


print("")
print("polimorfismo...")
# Usaremos la clase Person para demostrar el polimorfismo
# en el que varias clases heredan de la misma clase pero se comportan de diferentes maneras


class Person:
    def pay_bill(self):
        raise NotImplementedError

# Millionaire hereda de Persona


class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")

# Grad Student también hereda de la clase Persona


class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")


print("")
print("Asignatura: Zoo..")


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()
