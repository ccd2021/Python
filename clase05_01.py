class User1:		                    # declara una clase y dale el nombre User
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0


carlos = User1()
alberto = User1()

print(carlos.name)   # salida: Michael
print(alberto.name)  # salida: Michael


class User2:
    def __init__(self, username, email_address):    # ahora nuestro método tiene 2 parametros!
        self.name = username  # y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		            # y el atributo email
        # el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer parámetro
        self.account_balance = 0

    # agrega el método deposit

    def make_deposit(self, amount):  # toma un argumento que es el monto del depósito
        # la cuenta del usuario específico aumenta por la cantidad del valor recibido
        self.account_balance += amount
        return self

    # resta el método deposit
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    # Muestra saldo
    def display_user_balance(self, amount):
        self.account_balance
        print(self.name, ' Saldo cuenta es:', self.account_balance)
        return self


class User:
    def __init__(self, username, email_address):    # ahora nuestro método tiene 2 parametros!
        self.name = username  # y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		            # y el atributo email
        # el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer parámetro
        self.account_balance = 0

    # agrega el método deposit

    def make_deposit(self, amount):  # toma un argumento que es el monto del depósito
        # la cuenta del usuario específico aumenta por la cantidad del valor recibido
        self.account_balance += amount

    # resta el método deposit
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    # Muestra saldo
    def display_user_balance(self, amount):
        print(self.account_balance)


guido = User("carlos carrasco", "ccd@python.com")
monty = User("Alberto duarte", "aad@python.com")
print(guido.name)  # salida: Guido van Rossum
print(monty.name)  # salida: Monty Python

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)  # salida: 300
print(monty.account_balance)  # salida: 50

print("")
print("Tarea")

usr1 = User("Carlos Carrasco", "aaa@ccd.cl")
usr2 = User("Alberto Guzman", "bbb@ccd.cl")
usr3 = User("Pamela Fuentes", "ccc@ccd.cl")

print(usr1.name, ", ", usr2.name, ", ", usr3.name)

usr1.make_deposit(10000)
usr1.make_deposit(20000)
usr1.make_deposit(30000)
usr1.make_withdrawal(50000)
print('El Saldo del cliente [', usr1.name, '] es ...$', usr1.account_balance)

usr2.make_deposit(25000)
usr2.make_deposit(25000)
usr2.make_withdrawal(48000)
usr2.make_withdrawal(1)
print('El Saldo del cliente [', usr2.name, '] es ...$', usr2.account_balance)

usr3.make_deposit(25000)
usr3.make_withdrawal(5000)
usr3.make_withdrawal(5000)
usr3.make_withdrawal(3000)
print('El Saldo del cliente [', usr3.name, '] es ...$', usr3.account_balance)


print("")
print("metodos de encadenamientos")

usr4 = User2("Carlos Carrasco", "aaa@ccd.cl")
usr5 = User2("Alberto Guzman", "bbb@ccd.cl")
usr6 = User2("Pamela Fuentes", "ccc@ccd.cl")

print(usr1.name, ", ", usr2.name, ", ", usr3.name)

usr4.make_deposit(10000).make_deposit(20000).make_deposit(
    30000).make_withdrawal(50000).display_user_balance(0)
usr5.make_deposit(25000).make_deposit(25000).make_withdrawal(
    48000).make_withdrawal(1).display_user_balance(0)
usr6.make_deposit(25000).make_withdrawal(5000).make_withdrawal(
    5000).make_withdrawal(3000).display_user_balance(0)
