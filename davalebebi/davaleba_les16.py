### TASK 1 უნივერსიტეტის სისტემა

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def introduce(self):
        raise NotImplementedError ('Not written in subclass')

class Student(Person):
    def __init__(self, first_name, last_name, status):
        super().__init__(first_name, last_name)
        self.status = status
    def introduce(self):
        print(f'Hello, my name is {self.first_name} {self.last_name} and I am {self.status}')

class Lecturer(Person):
    def __init__(self, first_name, last_name, status):
        super().__init__(first_name, last_name)
        self.status = status

    def introduce(self):
        print(f'Hello, my name is {self.first_name} {self.last_name} and I am {self.status}')


person_1 = Student('John', 'Doe', 'Student')
person_2 = Lecturer('Lado', 'Doe', 'Lecturer')
person_1.introduce()
person_2.introduce()



### Task 2 სოციალური ქსელის პროფილი


class Profile:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password

    def check_password(self, password):
        return password == self.__password
    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            return True
        else:
            print("password not match")
            return False


user_1 = Profile('Jondo', 'jondo123@yahoo.com', 'jondo123')
print(user_1.check_password('jondo123'))
print(user_1.check_password('jondo1234'))
user_1.change_password('jondo1234', 'jondo321')
user_1.change_password('jondo123', 'jondo321')


### Task 3 ონლაინ მაღაზიის პროდუქტი


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, new_price):

        if new_price <= 0:
            print("Price must be positive")
        else:
            self.__price = new_price





product_1 = Product('Watch', 500)
print(product_1.name)
print(product_1.price)
product_1.price = 100
print(product_1.price)


### TASK 4  გადახდის სისტემა


class CreditCardPayment:
    def payment (self, amount):
        print (f'თქვენ გადაიხადეთ {amount} ლარო, საკრედიტო ბარათის გამოყენებით')

class Paypal:
    def payment (self, amount):
        print (f'თქვენ გადაიხადეთ {amount} ლარო, PayPal -ის გამოყენებით')

class Cypto:
    def payment (self, amount):
        print(f'თქვენ გადაიხადეთ {amount} ლარო, Crypto საფულის გამოყენებით')

payment_1 = CreditCardPayment()
payment_2 = Paypal()
payment_3 = Cypto()

payment_1.payment(100)
payment_2.payment(200)
payment_3.payment(300)




### TASK 5

class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars


c_1 = Car('BMW')
c_2 = Car('Mercedec')
c_3 = Car('Volga')

print(Car.get_total_cars())























